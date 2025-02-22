import numpy as np
from pandas.testing import assert_frame_equal

from pymove.core.pandas_discrete import PandasDiscreteMoveDataFrame
from pymove.utils.constants import (
    DATETIME,
    DIST_TO_PREV,
    INDEX_GRID,
    LATITUDE,
    LOCAL_LABEL,
    LONGITUDE,
    PREV_LOCAL,
    SPEED_TO_PREV,
    TID_STAT,
    TIME_TO_PREV,
    TRAJ_ID,
)


def test_discretize_based_grid():
    discrete_df = PandasDiscreteMoveDataFrame(
        data={DATETIME: ['2020-01-01 01:08:29',
                         '2020-01-05 01:13:24',
                         '2020-01-06 02:21:53',
                         '2020-01-06 03:34:48',
                         '2020-01-08 05:55:41'],
              LATITUDE: [3.754245,
                         3.150849,
                         3.754249,
                         3.165933,
                         3.920178],
              LONGITUDE: [38.3456743,
                          38.6913486,
                          38.3456743,
                          38.2715962,
                          38.5161605],
              TRAJ_ID: ['pwe-5089',
                        'xjt-1579',
                        'tre-1890',
                        'xjt-1579',
                        'pwe-5089'],
              LOCAL_LABEL: [1, 4, 2, 16, 32]},
    )

    expected = PandasDiscreteMoveDataFrame(
        data={DATETIME: ['2020-01-01 01:08:29',
                         '2020-01-08 05:55:41',
                         '2020-01-06 02:21:53',
                         '2020-01-05 01:13:24',
                         '2020-01-06 03:34:48'],
              LATITUDE: [3.754245,
                         3.920178,
                         3.754249,
                         3.150849,
                         3.165933],
              LONGITUDE: [38.3456743,
                          38.5161605,
                          38.3456743,
                          38.6913486,
                          38.2715962],
              TRAJ_ID: ['pwe-5089',
                        'pwe-5089',
                        'tre-1890',
                        'xjt-1579',
                        'xjt-1579'],
              LOCAL_LABEL: [1, 32, 2, 4, 16],
              INDEX_GRID: [754, 2407, 754, 3956, 1]},
    )

    discrete_df.discretize_based_grid()

    assert_frame_equal(discrete_df, expected)


def test_generate_prev_local_features():
    discrete_df = PandasDiscreteMoveDataFrame(
        data={DATETIME: ['2020-01-01 01:08:29',
                         '2020-01-01 01:10:29',
                         '2020-01-01 10:15:00',
                         '2020-01-05 01:13:24',
                         '2020-01-06 02:21:53',
                         ],
              LATITUDE: [3.754245,
                         3.150849,
                         3.754249,
                         3.165933,
                         3.920178,
                         ],
              LONGITUDE: [38.3456743,
                          38.6913486,
                          38.3456743,
                          38.2715962,
                          38.5161605,
                          ],
              TRAJ_ID: ['pwe-5089',
                        'pwe-5089',
                        'pwe-5089',
                        'pwe-5089',
                        'pwe-5089',
                        ],
              LOCAL_LABEL: [1.0, 2.0, 1.0, 2.0, 1.0]},
    )

    expected = PandasDiscreteMoveDataFrame(
        data={
            TRAJ_ID: ['pwe-5089',
                      'pwe-5089',
                      'pwe-5089',
                      'pwe-5089',
                      'pwe-5089',],
            DATETIME: ['2020-01-01 01:08:29',
                       '2020-01-01 01:10:29',
                       '2020-01-01 10:15:00',
                       '2020-01-05 01:13:24',
                       '2020-01-06 02:21:53',],
            LATITUDE: [3.754245,
                       3.150849,
                       3.754249,
                       3.165933,
                       3.920178,
                       ],
            LONGITUDE: [38.3456743,
                        38.6913486,
                        38.3456743,
                        38.2715962,
                        38.5161605,
                        ],
            LOCAL_LABEL: [1.0, 2.0, 1.0, 2.0, 1.0],
            PREV_LOCAL: [np.nan, 1.0, 2.0, 1.0, 2.0]},
    )

    discrete_df.generate_prev_local_features()
    print(discrete_df)
    assert_frame_equal(discrete_df, expected)


def test_generate_tid_based_statistics():
    discrete_df = PandasDiscreteMoveDataFrame(
        data={
            TRAJ_ID: ['pwe-5089',
                      'pwe-5089',
                      'pwe-5089',
                      'pwe-5089',
                      'pwe-5089'
                      ],
            DATETIME: ['2020-01-01 01:08:29',
                       '2020-01-01 01:10:29',
                       '2020-01-01 10:15:00',
                       '2020-01-05 01:13:24',
                       '2020-01-06 02:21:53',
                       ],
            LATITUDE: [3.754245,
                       3.150849,
                       3.754249,
                       3.165933,
                       3.920178,
                       ],
            LONGITUDE: [38.3456743,
                        38.6913486,
                        38.3456743,
                        38.2715962,
                        38.5161605
                        ],
            LOCAL_LABEL: [1.0, 2.0, 1.0, 2.0, 1.0],
            PREV_LOCAL: [np.nan, 1.0, 2.0, 1.0, 2.0]}
    )

    expected = PandasDiscreteMoveDataFrame(
        data={
            TRAJ_ID: ['pwe-5089',
                      'pwe-5089',
                      'pwe-5089',
                      'pwe-5089',
                      'pwe-5089',
                      ],
            DATETIME: ['2020-01-01 01:08:29',
                       '2020-01-01 01:10:29',
                       '2020-01-01 10:15:00',
                       '2020-01-05 01:13:24',
                       '2020-01-06 02:21:53',
                       ],
            LATITUDE: [3.754245,
                       3.150849,
                       3.754249,
                       3.165933,
                       3.920178,
                       ],
            LONGITUDE: [38.3456743,
                        38.6913486,
                        38.3456743,
                        38.2715962,
                        38.5161605,
                        ],
            LOCAL_LABEL: [1.0, 2.0, 1.0, 2.0, 1.0],
            PREV_LOCAL: [np.nan, 1.0, 2.0, 1.0, 2.0],
            DIST_TO_PREV: [np.nan, 77289.911988, 77290.298056,
                           65932.426141, 88150.855250],
            TIME_TO_PREV: [np.nan, 120.0, 32671.0, 313104.0, 90509.0],
            SPEED_TO_PREV: [np.nan, 644.082600, 2.365716, 0.210577, 0.973946],
            TID_STAT: [1, 1, 1, 1, 1]},
    )

    discrete_df.generate_tid_based_statistics()
    print(discrete_df)
    print(expected)
    assert_frame_equal(discrete_df, expected)
