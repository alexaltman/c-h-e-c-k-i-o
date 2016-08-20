OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):

    input_ = str(x) + str(y)

    pre_dict = {"conjunction": 0,
                "disjunction": 1,
                "implication": 2,
                "exclusive": 3,
                "equivalence": 4
                }

    dict_ = { "00": [{ "conjunction": 0}, {"disjunction": 0}, {"implication": 1}, {"exclusive": 0}, {"equivalence": 1}],
             "10": [{ "conjunction": 0}, {"disjunction": 1}, {"implication": 0}, {"exclusive": 1}, {"equivalence": 0}],
             "01": [{ "conjunction": 0}, {"disjunction": 1}, {"implication": 1}, {"exclusive": 1}, {"equivalence": 0}],
             "11": [{ "conjunction": 1}, {"disjunction": 1}, {"implication": 1}, {"exclusive": 0}, {"equivalence": 1}],
            }

    return dict_[input_][pre_dict[operation]][operation]
