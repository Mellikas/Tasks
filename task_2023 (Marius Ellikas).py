def find_index_of_darkest_street_light(road_length, not_working_street_lights):
    stree_light_number = int(road_length / 20) + 1
    all_lights = list(range(0, stree_light_number))

    working_lights = all_lights
    for light in not_working_street_lights:
        del working_lights[working_lights.index(light)]

    not_working_lights_ilumination = {}

    for n_light in not_working_street_lights:
        distances_from_all_working_light = []

        for w_light in working_lights:
            index_distance = n_light - w_light

            if index_distance > 0:
                distances_from_all_working_light.append(index_distance * 20)
            else:
                distances_from_all_working_light.append((-index_distance) * 20)

        n_light_illumination_sum = 0
        for distance in distances_from_all_working_light:
            illumination = 3 ** (-(distance / 90) ** 2)
            if illumination >= 0.01:
                n_light_illumination_sum += illumination
            else:
                pass
        not_working_lights_ilumination[n_light] = n_light_illumination_sum

    lowest_illumination = min(not_working_lights_ilumination.values())

    lowest_dic = {}
    for k, v in not_working_lights_ilumination.items():
        if v == lowest_illumination:
            lowest_dic[k] = v

    result = min(lowest_dic)

    return result


if __name__ == "__main__":
    # This is an example test. When evaluating the task, more will be added:
    assert find_index_of_darkest_street_light(road_length=200, not_working_street_lights=[4, 5, 6]) == 5
    print("ALL TESTS PASSED")
