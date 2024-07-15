from dataclasses import dataclass, field
from typing import List, Dict, Iterable

from modules.interfaces.bytes_parser_interface import CppStruct


@dataclass
class EstimatedCollection:
    @dataclass
    class EstimatedEntity:
        structs: List[CppStruct] = field(default_factory=list)

    estimated_map: Dict[str, EstimatedEntity] = field(default_factory=dict)

    def all_structs(self) -> Iterable[CppStruct]:
        for entity in self.estimated_map.values():
            for struct in entity.structs:
                yield struct

    def add(self, key: str, structs: List[CppStruct]) -> None:
        if key not in self.estimated_map:
            self.estimated_map[key] = self.EstimatedEntity()
        self.estimated_map[key].structs = structs
