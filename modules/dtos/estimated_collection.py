from dataclasses import dataclass, field
from typing import List, Dict, Iterable, Tuple

from modules.aliases.aliases import CppStruct, SourceKey


@dataclass
class EstimatedCollection:
    @dataclass
    class EstimatedEntity:
        cpp_struct_list: List[CppStruct] = field(default_factory=list)

    # map where key = source key, value = EstimatedEntity aka cpp_struct_list
    estimated_map: Dict[SourceKey, EstimatedEntity] = field(default_factory=dict)

    def all_structs(self, separate_keys: bool = True) -> Iterable[Tuple[SourceKey, CppStruct]]:
        for key, entity in self.estimated_map.items():
            for index, struct in enumerate(entity.cpp_struct_list):
                modified_key = f"{key}.{index + 1}" if separate_keys else key
                yield modified_key, struct

    def add(self, key: SourceKey, structs: List[CppStruct]) -> None:
        if key not in self.estimated_map:
            self.estimated_map[key] = self.EstimatedEntity()
        self.estimated_map[key].cpp_struct_list = structs
