from typing import Dict, List, Tuple, Union
import collections
import itertools
import textwrap

class Keyboard(collections.UserDict):
    """"""
    @property
    def n_rows(self):
        return int(max(pos.real for pos in self.values()) + 1)

    @property
    def n_columns(self):
        return int(max(pos.imag for pos in self.values()) + 1)

    @property
    def shape(self):
        return (self.n_rows, self.n_columns)

    def char_distance(self, c1: str, c2: str) -> float:
        """Euclidean distance between two characters."""
        return abs(self[c1] - self[c2]) if c1 != c2 else 0.0


    def typing_distance(self, word: str) -> float:
        return sum(self.char_distance(c1, c2) for c1, c2 in zip(word, word[1:]))

    @classmethod
    def from_coordinates(
        cls,
        coordinates: Dict[str, Tuple[int, int]],
        staggering: Union[float, List] = 0,
        horizontal_pitch=1,
        vertical_pitch=1,
    ):
        """
        Parameters
        ----------
        coordinates
            A dictionary specifying the (row, col) location of each character. The origin is
            assumed to be at the top-left corner.
        staggering
            Controls the amount of staggering between consecutive rows. The amount of staggering is
            the same between pair of consecutive rows if a single number is specified. Variable
            amounts of staggering can be specified by providing a list of length `n_rows - 1`,
            within which the ith element corresponds the staggering between rows `i` and `i + 1`.
        horizontal_pitch
            The horizontal distance between the center of two adjacent keys.
        vertical_pitch
            The vertical distance between the center of two adjacent keys.
        """
        if isinstance(staggering, list):
            staggering = list(itertools.accumulate(staggering, initial=0))

        return cls(
            {
                char: complex(
                    i * vertical_pitch,
                    j * horizontal_pitch
                    + (
                        staggering[i]
                        if isinstance(staggering, list)
                        else i * staggering
                    ),
                )
                for char, (i, j) in coordinates.items()
            }
        )

    @classmethod
    def from_grid(
        cls,
        grid: str,
        staggering: Union[float, List] = 0,
        horizontal_pitch=1,
        vertical_pitch=1,
    ):
        """
        Parameters
        ----------
        grid
            A keyboard layout specified as a grid separated by spaces. See the examples to
            understand the format.
        staggering
            Controls the amount of staggering between consecutive rows. The amount of staggering is
            the same between pair of consecutive rows if a single number is specified. Variable
            amounts of staggering can be specified by providing a list of length `n_rows - 1`,
            within which the ith element corresponds the staggering between rows `i` and `i + 1`.
        horizontal_pitch
            The horizontal distance between the center of two adjacent keys.
        vertical_pitch
            The vertical distance between the center of two adjacent keys.
        """
        return cls.from_coordinates(
            coordinates={
                char: (i, j)
                for i, row in enumerate(filter(len, textwrap.dedent(grid).splitlines()))
                for j, char in enumerate(row[::2])
                if char
            },
            staggering=staggering,
            horizontal_pitch=horizontal_pitch,
            vertical_pitch=vertical_pitch,
        )

    def __repr__(self):
        rows = [[] for _ in range(self.n_rows)]
        reverse_layout = {
            (int(pos.real), int(pos.imag)): char for char, pos in self.items()
        }
        for i, j in sorted(reverse_layout.keys()):
            rows[i].extend([" "] * (j - len(rows[i])))
            rows[i].append(reverse_layout[i, j])
        return "\n".join(" ".join(row) for row in rows)



