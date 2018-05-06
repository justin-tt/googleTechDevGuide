def calculateVolume(lake_profile):
    # we need to find the highest point in this island (there may be more than one point that has the same highest height)
    # e.g. in a peak [1,3,2,4,1,3,1,4,5,2,2,1,4,2,2]
    # highest peak == 5, at index [8]

    def find_highest_peak(lake_profile):
        max_peak_height = 0
        positions = []
        for idx, val in enumerate(lake_profile):
            if val > max_peak_height:
                max_peak_height = val
                positions = []
                positions.append(idx)
            elif val == max_peak_height:
                positions.append(idx)
        # print(max_peak_height, positions)
        return (max_peak_height, positions)

    # assert(find_highest_peak(lake_profile)) == (5, [8])
    # assert(find_highest_peak([1,3,4,5,4,5,3,1])) == (5, [3, 5])
    highest_peaks = find_highest_peak(lake_profile)

    # find successive peaks, defined as higher or equal to the one preceding it 
    # start from each end and converge on the highest peak.
    # e.g. 1, 3, 4, 4, 5 from the left hand side.
    # 2, 2, 4, 5 from the right hand side.
    def find_left_successive_peaks(lake_profile, highest_peaks):
        successive_peaks = {}
        peak_height = 0
        for idx, val in enumerate(lake_profile[0:highest_peaks[1][0]]):
            if val >= peak_height:
                peak_height = val
                successive_peaks[idx] = val
        # print(successive_peaks)
        return successive_peaks

    def find_right_successive_peaks(lake_profile, highest_peaks):
        successive_peaks = {}
        peak_height = 0
        length = len(lake_profile)
        for idx, val in enumerate(reversed(lake_profile[highest_peaks[1][-1]+1:length])):
            if val >= peak_height:
                peak_height = val
                successive_peaks[length-idx-1] = val
        # print(successive_peaks)
        return successive_peaks


    def map_lake_profile(lake_profile):
        dict_lake_profile = {}
        for idx, val in enumerate(lake_profile):
            dict_lake_profile[idx] = val
        return dict_lake_profile
    # print(map_lake_profile(lake_profile))
    
    # if there is more than 1 highest peak we need to also find the valleys in between

    def fill_peaks(left_successive_peaks, right_successive_peaks, highest_peaks, dict_lake_profile):
        water_vol_filled = {}
        # for single highest peak
        peak_height = 0
        # left side
        for i in range(highest_peaks[1][0]):
            if i in left_successive_peaks:
                peak_height = left_successive_peaks[i]
            if i not in left_successive_peaks:
                water_vol_filled[i] = peak_height - dict_lake_profile[i]
        # right side
        peak_height = 0 
        for i in range(len(dict_lake_profile)-1, highest_peaks[1][-1], -1):
            if i in right_successive_peaks:
                peak_height = right_successive_peaks[i]
            if i not in right_successive_peaks:
                water_vol_filled[i] = peak_height - dict_lake_profile[i]
        # print(water_vol_filled)
        if len(highest_peaks[1]) == 1:
            return water_vol_filled
        else:
        # for multiple peaks
            peak_height = highest_peaks[0]
            for i in range(highest_peaks[1][0], highest_peaks[1][-1]):
                if i not in highest_peaks[1]:
                    water_vol_filled[i] = peak_height - dict_lake_profile[i]
                
            # print(water_vol_filled)
            return water_vol_filled

    dict_lake_profile = map_lake_profile(lake_profile)
    left_successive_peaks = find_left_successive_peaks(lake_profile, highest_peaks)
    right_successive_peaks = find_right_successive_peaks(lake_profile, highest_peaks)
    water_vol_filled_profile = fill_peaks(left_successive_peaks, right_successive_peaks, highest_peaks, dict_lake_profile)
    # for each of these successive peaks, the valleys in between need to match the amount of water

    total_vol_filled = 0
    for key in water_vol_filled_profile:
        total_vol_filled += water_vol_filled_profile[key]
    return total_vol_filled



assert calculateVolume([1,3,2,4,1,3,1,4,5,2,2,1,4,2,2]) == 15
assert calculateVolume([1,3,2,4,5,4,5,4,5,3,1]) == 3
assert calculateVolume([1,3,2,4,5,4,6,4,5,3,1]) == 3
