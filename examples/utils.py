from __future__ import annotations

import aiosu

score = aiosu.models.Score()
diff_atribs = aiosu.models.BeatmapDifficultyAttributes()

acc_calc = aiosu.utils.accuracy.OsuAccuracyCalculator()
accuracy: float = acc_calc.calculate(score)
accuracy_weighted: float = acc_calc.calculate_weighted(score)

pp_calc = aiosu.utils.performance.OsuPerformanceCalculator(diff_atribs)
pp_atribs: aiosu.models.OsuPerformanceAttributes = pp_calc.calculate(score)
