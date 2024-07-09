from dataclasses import dataclass, field


@dataclass
class EstimateSettings:
    matches_percent: int = field(default=0)

    @property
    def matches_percent(self) -> int:
        return self.matches_percent

    @matches_percent.setter
    def matches_percent(self, value: int):
        if 0 <= value <= 100:
            self.matches_percent = value
        else:
            raise ValueError("matches_percent must be between 0 and 100")


class EstimatorInterface:
    pass
