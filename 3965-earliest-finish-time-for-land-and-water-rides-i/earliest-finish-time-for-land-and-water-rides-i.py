class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration,
                           waterStartTime, waterDuration):

        ans = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):

                # Land -> Water
                land_finish = landStartTime[i] + landDuration[i]
                water_begin = max(land_finish, waterStartTime[j])
                ans = min(ans, water_begin + waterDuration[j])

                # Water -> Land
                water_finish = waterStartTime[j] + waterDuration[j]
                land_begin = max(water_finish, landStartTime[i])
                ans = min(ans, land_begin + landDuration[i])

        return ans