import io

from modules.interfaces.estimate_result_printer_interface import EstimateResultPrinterInterface
from modules.interfaces.estimator_interface import EstimateUniqueFieldsResult
from settings import Settings


class EstimateResultPrinter(EstimateResultPrinterInterface):
    @staticmethod
    def print(result: EstimateUniqueFieldsResult, cfg: Settings.Estimate, stream: io.TextIOBase = io.StringIO()):
        for field_name, field_result in result.unique_fields.items():
            print(f"field: {field_name}", file=stream)
            for value, estimate_unique_field_values_result in field_result.percentage_of_values.items():
                if (cfg.result_printer.only_filtered_view and
                        estimate_unique_field_values_result.freq < cfg.matches_percent):
                    continue
                print(
                    f"\tvalue: {value} - {estimate_unique_field_values_result.freq:.2f}%' +"
                    f"'\tincluded source keys: {sorted(estimate_unique_field_values_result.included_source_keys)}",
                    file=stream
                )

