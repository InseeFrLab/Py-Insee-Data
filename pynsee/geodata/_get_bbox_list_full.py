def _get_bbox_list_full(crs="EPSG:4326"):

    if crs == "EPSG:4326":
        bbox_list = [
            (-62.0, 13.0, -61.0, 14.5),
            (-62.0, 14.5, -61.0, 16.0),
            (-62.0, 16.0, -61.0, 17.5),
            (-61.0, 13.0, -60.0, 14.5),
            (-61.0, 14.5, -60.0, 16.0),
            (-55.0, 1.0, -54.0, 2.5),
            (-55.0, 2.5, -54.0, 4.0),
            (-55.0, 4.0, -54.0, 5.5),
            (-55.0, 5.5, -54.0, 7.0),
            (-54.0, 1.0, -53.0, 2.5),
            (-54.0, 2.5, -53.0, 4.0),
            (-54.0, 4.0, -53.0, 5.5),
            (-54.0, 5.5, -53.0, 7.0),
            (-53.0, 1.0, -52.0, 2.5),
            (-53.0, 2.5, -52.0, 4.0),
            (-53.0, 4.0, -52.0, 5.5),
            (-53.0, 5.5, -52.0, 7.0),
            (-52.0, 1.0, -51.0, 2.5),
            (-52.0, 2.5, -51.0, 4.0),
            (-52.0, 4.0, -51.0, 5.5),
            (-52.0, 5.5, -51.0, 7.0),
            (-6.0, 47.5, -5.0, 49.0),
            (-5.0, 47.5, -4.0, 49.0),
            (-4.0, 46.0, -3.0, 47.5),
            (-4.0, 47.5, -3.0, 49.0),
            (-3.0, 46.0, -2.0, 47.5),
            (-3.0, 47.5, -2.0, 49.0),
            (-2.0, 41.5, -1.0, 43.0),
            (-2.0, 43.0, -1.0, 44.5),
            (-2.0, 44.5, -1.0, 46.0),
            (-2.0, 46.0, -1.0, 47.5),
            (-2.0, 47.5, -1.0, 49.0),
            (-2.0, 49.0, -1.0, 50.5),
            (-1.0, 41.5, 0.0, 43.0),
            (-1.0, 43.0, 0.0, 44.5),
            (-1.0, 44.5, 0.0, 46.0),
            (-1.0, 46.0, 0.0, 47.5),
            (-1.0, 47.5, 0.0, 49.0),
            (-1.0, 49.0, 0.0, 50.5),
            (0.0, 41.5, 1.0, 43.0),
            (0.0, 43.0, 1.0, 44.5),
            (0.0, 44.5, 1.0, 46.0),
            (0.0, 46.0, 1.0, 47.5),
            (0.0, 47.5, 1.0, 49.0),
            (0.0, 49.0, 1.0, 50.5),
            (1.0, 41.5, 2.0, 43.0),
            (1.0, 43.0, 2.0, 44.5),
            (1.0, 44.5, 2.0, 46.0),
            (1.0, 46.0, 2.0, 47.5),
            (1.0, 47.5, 2.0, 49.0),
            (1.0, 49.0, 2.0, 50.5),
            (1.0, 50.5, 2.0, 52.0),
            (2.0, 41.5, 3.0, 43.0),
            (2.0, 43.0, 3.0, 44.5),
            (2.0, 44.5, 3.0, 46.0),
            (2.0, 46.0, 3.0, 47.5),
            (2.0, 47.5, 3.0, 49.0),
            (2.0, 49.0, 3.0, 50.5),
            (2.0, 50.5, 3.0, 52.0),
            (3.0, 41.5, 4.0, 43.0),
            (3.0, 43.0, 4.0, 44.5),
            (3.0, 44.5, 4.0, 46.0),
            (3.0, 46.0, 4.0, 47.5),
            (3.0, 47.5, 4.0, 49.0),
            (3.0, 49.0, 4.0, 50.5),
            (3.0, 50.5, 4.0, 52.0),
            (4.0, 43.0, 5.0, 44.5),
            (4.0, 44.5, 5.0, 46.0),
            (4.0, 46.0, 5.0, 47.5),
            (4.0, 47.5, 5.0, 49.0),
            (4.0, 49.0, 5.0, 50.5),
            (4.0, 50.5, 5.0, 52.0),
            (5.0, 41.5, 6.0, 43.0),
            (5.0, 43.0, 6.0, 44.5),
            (5.0, 44.5, 6.0, 46.0),
            (5.0, 46.0, 6.0, 47.5),
            (5.0, 47.5, 6.0, 49.0),
            (5.0, 49.0, 6.0, 50.5),
            (6.0, 41.5, 7.0, 43.0),
            (6.0, 43.0, 7.0, 44.5),
            (6.0, 44.5, 7.0, 46.0),
            (6.0, 46.0, 7.0, 47.5),
            (6.0, 47.5, 7.0, 49.0),
            (6.0, 49.0, 7.0, 50.5),
            (7.0, 43.0, 8.0, 44.5),
            (7.0, 44.5, 8.0, 46.0),
            (7.0, 46.0, 8.0, 47.5),
            (7.0, 47.5, 8.0, 49.0),
            (7.0, 49.0, 8.0, 50.5),
            (8.0, 40.0, 9.0, 41.5),
            (8.0, 41.5, 9.0, 43.0),
            (8.0, 43.0, 9.0, 44.5),
            (8.0, 47.5, 9.0, 49.0),
            (8.0, 49.0, 9.0, 50.5),
            (9.0, 40.0, 10.0, 41.5),
            (9.0, 41.5, 10.0, 43.0),
            (9.0, 43.0, 10.0, 44.5),
            (45.0, -14.0, 46.0, -12.5),
            (55.0, -21.5, 56.0, -20.0),
        ]
    else:
        bbox_list = [
            (
                -6901808.429182961,
                1459732.2718804975,
                -6790488.938389688,
                1631643.4670073595,
            ),
            (
                -6901808.429182961,
                1631643.4670073595,
                -6790488.938389688,
                1804722.766257292,
            ),
            (
                -6901808.429182961,
                1804722.766257292,
                -6790488.938389688,
                1979106.499724388,
            ),
            (
                -6790488.938389688,
                1459732.2718804975,
                -6679169.447596414,
                1631643.4670073595,
            ),
            (
                -6790488.938389688,
                1631643.4670073595,
                -6679169.447596414,
                1804722.766257292,
            ),
            (
                -6122571.993630046,
                111325.14286638486,
                -6011252.502836772,
                278387.0759542342,
            ),
            (
                -6122571.993630046,
                278387.0759542342,
                -6011252.502836772,
                445640.1096560266,
            ),
            (
                -6122571.993630046,
                445640.1096560266,
                -6011252.502836772,
                613199.6633499706,
            ),
            (
                -6122571.993630046,
                613199.6633499706,
                -6011252.502836772,
                781182.2141882492,
            ),
            (
                -6011252.502836772,
                111325.14286638486,
                -5899933.012043499,
                278387.0759542342,
            ),
            (
                -6011252.502836772,
                278387.0759542342,
                -5899933.012043499,
                445640.1096560266,
            ),
            (
                -6011252.502836772,
                445640.1096560266,
                -5899933.012043499,
                613199.6633499706,
            ),
            (
                -6011252.502836772,
                613199.6633499706,
                -5899933.012043499,
                781182.2141882492,
            ),
            (
                -5899933.012043499,
                111325.14286638486,
                -5788613.521250226,
                278387.0759542342,
            ),
            (
                -5899933.012043499,
                278387.0759542342,
                -5788613.521250226,
                445640.1096560266,
            ),
            (
                -5899933.012043499,
                445640.1096560266,
                -5788613.521250226,
                613199.6633499706,
            ),
            (
                -5899933.012043499,
                613199.6633499706,
                -5788613.521250226,
                781182.2141882492,
            ),
            (
                -5788613.521250226,
                111325.14286638486,
                -5677294.030456952,
                278387.0759542342,
            ),
            (
                -5788613.521250226,
                278387.0759542342,
                -5677294.030456952,
                445640.1096560266,
            ),
            (
                -5788613.521250226,
                445640.1096560266,
                -5677294.030456952,
                613199.6633499706,
            ),
            (
                -5788613.521250226,
                613199.6633499706,
                -5677294.030456952,
                781182.2141882492,
            ),
            (
                -667916.9447596414,
                6024072.119373783,
                -556597.4539663679,
                6274861.394006577,
            ),
            (
                -556597.4539663679,
                6024072.119373783,
                -445277.96317309426,
                6274861.394006577,
            ),
            (
                -445277.96317309426,
                5780349.220256351,
                -333958.4723798207,
                6024072.119373783,
            ),
            (
                -445277.96317309426,
                6024072.119373783,
                -333958.4723798207,
                6274861.394006577,
            ),
            (
                -333958.4723798207,
                5780349.220256351,
                -222638.98158654713,
                6024072.119373783,
            ),
            (
                -333958.4723798207,
                6024072.119373783,
                -222638.98158654713,
                6274861.394006577,
            ),
            (
                -222638.98158654713,
                5086373.649287362,
                -111319.49079327357,
                5311971.846945471,
            ),
            (
                -222638.98158654713,
                5311971.846945471,
                -111319.49079327357,
                5543147.203861799,
            ),
            (
                -222638.98158654713,
                5543147.203861799,
                -111319.49079327357,
                5780349.220256351,
            ),
            (
                -222638.98158654713,
                5780349.220256351,
                -111319.49079327357,
                6024072.119373783,
            ),
            (
                -222638.98158654713,
                6024072.119373783,
                -111319.49079327357,
                6274861.394006577,
            ),
            (
                -222638.98158654713,
                6274861.394006577,
                -111319.49079327357,
                6533321.567837933,
            ),
            (-111319.49079327357, 5086373.649287362, 0.0, 5311971.846945471),
            (-111319.49079327357, 5311971.846945471, 0.0, 5543147.203861799),
            (-111319.49079327357, 5543147.203861799, 0.0, 5780349.220256351),
            (-111319.49079327357, 5780349.220256351, 0.0, 6024072.119373783),
            (-111319.49079327357, 6024072.119373783, 0.0, 6274861.394006577),
            (-111319.49079327357, 6274861.394006577, 0.0, 6533321.567837933),
            (0.0, 5086373.649287362, 111319.49079327357, 5311971.846945471),
            (0.0, 5311971.846945471, 111319.49079327357, 5543147.203861799),
            (0.0, 5543147.203861799, 111319.49079327357, 5780349.220256351),
            (0.0, 5780349.220256351, 111319.49079327357, 6024072.119373783),
            (0.0, 6024072.119373783, 111319.49079327357, 6274861.394006577),
            (0.0, 6274861.394006577, 111319.49079327357, 6533321.567837933),
            (
                111319.49079327357,
                5086373.649287362,
                222638.98158654713,
                5311971.846945471,
            ),
            (
                111319.49079327357,
                5311971.846945471,
                222638.98158654713,
                5543147.203861799,
            ),
            (
                111319.49079327357,
                5543147.203861799,
                222638.98158654713,
                5780349.220256351,
            ),
            (
                111319.49079327357,
                5780349.220256351,
                222638.98158654713,
                6024072.119373783,
            ),
            (
                111319.49079327357,
                6024072.119373783,
                222638.98158654713,
                6274861.394006577,
            ),
            (
                111319.49079327357,
                6274861.394006577,
                222638.98158654713,
                6533321.567837933,
            ),
            (
                111319.49079327357,
                6533321.567837933,
                222638.98158654713,
                6800125.454397307,
            ),
            (
                222638.98158654713,
                5086373.649287362,
                333958.4723798207,
                5311971.846945471,
            ),
            (
                222638.98158654713,
                5311971.846945471,
                333958.4723798207,
                5543147.203861799,
            ),
            (
                222638.98158654713,
                5543147.203861799,
                333958.4723798207,
                5780349.220256351,
            ),
            (
                222638.98158654713,
                5780349.220256351,
                333958.4723798207,
                6024072.119373783,
            ),
            (
                222638.98158654713,
                6024072.119373783,
                333958.4723798207,
                6274861.394006577,
            ),
            (
                222638.98158654713,
                6274861.394006577,
                333958.4723798207,
                6533321.567837933,
            ),
            (
                222638.98158654713,
                6533321.567837933,
                333958.4723798207,
                6800125.454397307,
            ),
            (
                333958.4723798207,
                5086373.649287362,
                445277.96317309426,
                5311971.846945471,
            ),
            (
                333958.4723798207,
                5311971.846945471,
                445277.96317309426,
                5543147.203861799,
            ),
            (
                333958.4723798207,
                5543147.203861799,
                445277.96317309426,
                5780349.220256351,
            ),
            (
                333958.4723798207,
                5780349.220256351,
                445277.96317309426,
                6024072.119373783,
            ),
            (
                333958.4723798207,
                6024072.119373783,
                445277.96317309426,
                6274861.394006577,
            ),
            (
                333958.4723798207,
                6274861.394006577,
                445277.96317309426,
                6533321.567837933,
            ),
            (
                333958.4723798207,
                6533321.567837933,
                445277.96317309426,
                6800125.454397307,
            ),
            (
                445277.96317309426,
                5311971.846945471,
                556597.4539663679,
                5543147.203861799,
            ),
            (
                445277.96317309426,
                5543147.203861799,
                556597.4539663679,
                5780349.220256351,
            ),
            (
                445277.96317309426,
                5780349.220256351,
                556597.4539663679,
                6024072.119373783,
            ),
            (
                445277.96317309426,
                6024072.119373783,
                556597.4539663679,
                6274861.394006577,
            ),
            (
                445277.96317309426,
                6274861.394006577,
                556597.4539663679,
                6533321.567837933,
            ),
            (
                445277.96317309426,
                6533321.567837933,
                556597.4539663679,
                6800125.454397307,
            ),
            (
                556597.4539663679,
                5086373.649287362,
                667916.9447596414,
                5311971.846945471,
            ),
            (
                556597.4539663679,
                5311971.846945471,
                667916.9447596414,
                5543147.203861799,
            ),
            (
                556597.4539663679,
                5543147.203861799,
                667916.9447596414,
                5780349.220256351,
            ),
            (
                556597.4539663679,
                5780349.220256351,
                667916.9447596414,
                6024072.119373783,
            ),
            (
                556597.4539663679,
                6024072.119373783,
                667916.9447596414,
                6274861.394006577,
            ),
            (
                556597.4539663679,
                6274861.394006577,
                667916.9447596414,
                6533321.567837933,
            ),
            (
                667916.9447596414,
                5086373.649287362,
                779236.435552915,
                5311971.846945471,
            ),
            (
                667916.9447596414,
                5311971.846945471,
                779236.435552915,
                5543147.203861799,
            ),
            (
                667916.9447596414,
                5543147.203861799,
                779236.435552915,
                5780349.220256351,
            ),
            (
                667916.9447596414,
                5780349.220256351,
                779236.435552915,
                6024072.119373783,
            ),
            (
                667916.9447596414,
                6024072.119373783,
                779236.435552915,
                6274861.394006577,
            ),
            (
                667916.9447596414,
                6274861.394006577,
                779236.435552915,
                6533321.567837933,
            ),
            (
                779236.435552915,
                5311971.846945471,
                890555.9263461885,
                5543147.203861799,
            ),
            (
                779236.435552915,
                5543147.203861799,
                890555.9263461885,
                5780349.220256351,
            ),
            (
                779236.435552915,
                5780349.220256351,
                890555.9263461885,
                6024072.119373783,
            ),
            (
                779236.435552915,
                6024072.119373783,
                890555.9263461885,
                6274861.394006577,
            ),
            (
                779236.435552915,
                6274861.394006577,
                890555.9263461885,
                6533321.567837933,
            ),
            (
                890555.9263461885,
                4865942.279503176,
                1001875.4171394621,
                5086373.649287362,
            ),
            (
                890555.9263461885,
                5086373.649287362,
                1001875.4171394621,
                5311971.846945471,
            ),
            (
                890555.9263461885,
                5311971.846945471,
                1001875.4171394621,
                5543147.203861799,
            ),
            (
                890555.9263461885,
                6024072.119373783,
                1001875.4171394621,
                6274861.394006577,
            ),
            (
                890555.9263461885,
                6274861.394006577,
                1001875.4171394621,
                6533321.567837933,
            ),
            (
                1001875.4171394621,
                4865942.279503176,
                1113194.9079327357,
                5086373.649287362,
            ),
            (
                1001875.4171394621,
                5086373.649287362,
                1113194.9079327357,
                5311971.846945471,
            ),
            (
                1001875.4171394621,
                5311971.846945471,
                1113194.9079327357,
                5543147.203861799,
            ),
            (
                5009377.085697311,
                -1574216.548161465,
                5120696.576490585,
                -1402665.1899679275,
            ),
            (
                6122571.993630046,
                -2451599.0873778556,
                6233891.48442332,
                -2273030.92698769,
            ),
        ]

    return bbox_list
