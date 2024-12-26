import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor["name"]} should be vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor["name"]}"
                                       f" vaccine is outdatet")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{visitor["name"]} should hame a mask")
        return f"Welcome to {self.name}"
