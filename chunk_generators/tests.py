import pytest

from .generator_zero_chunks import generator_zero_chunks


class TestGenerateZeroChunks:
    """Tests for generator_zero_chunks generator"""

    def test_invalid_only_zero_chunks(self) -> None:
        with pytest.raises(Exception):
            list(generator_zero_chunks("0000-0000-0000-0000-0000"))

    @pytest.mark.parametrize(
        "test_code", ["B001-00AA-0001-0002-0007-AVCD", "B001-00AA-0001-0002"]
    )
    def test_invalid_code_length(self, test_code: str) -> None:
        with pytest.raises(Exception):
            list(generator_zero_chunks(test_code))

    def test_invalid_separator(self) -> None:
        test_code = "B001.00AA.0001.0002.0007"
        with pytest.raises(Exception):
            list(generator_zero_chunks(test_code))

    def test_invalid_chunk_length(self) -> None:
        test_code = "B001-00AA-0001-0002-00055"
        with pytest.raises(Exception):
            list(generator_zero_chunks(test_code))

    @pytest.mark.parametrize(
        "test_code",
        [
            "B001-00AA-0001-0000-0007",
            "0000-00AA-0001-0001-0007",
            "0000-0000-0000-0000-0007",
            "B001-0000-0001-0000-0007",
        ],
    )
    def test_invalid_zero_chunk_followed_by_non_zero(self, test_code) -> None:
        with pytest.raises(Exception):
            list(generator_zero_chunks(test_code))

    @pytest.mark.parametrize(
        "test_code,test_result",
        [
            (
                "B001-00AA-0001-0002-0007",
                [
                    "B001-00AA-0001-0002-0007",
                    "B001-00AA-0001-0002-0000",
                    "B001-00AA-0001-0000-0000",
                    "B001-00AA-0000-0000-0000",
                    "B001-0000-0000-0000-0000",
                ],
            ),
            (
                "B001-00AA-0000-0000-0000",
                ["B001-00AA-0000-0000-0000", "B001-0000-0000-0000-0000"],
            ),
            ("B001-0000-0000-0000-0000", ["B001-0000-0000-0000-0000"]),
        ],
    )
    def test_correct_replace(self, test_code, test_result) -> None:

        result = list(generator_zero_chunks(test_code))
        assert len(result) == len(test_result)
        for result_value, test_value in zip(result, test_result):
            assert result_value == test_value
