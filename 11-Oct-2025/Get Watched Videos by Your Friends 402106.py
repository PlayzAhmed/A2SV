# Problem: Get Watched Videos by Your Friends - https://leetcode.com/problems/get-watched-videos-by-your-friends/description/

class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, _id, level):
        friends_level = []
        watched = []
        q = deque([(_id, 0)])
        seen = set()

        while q:
            cur_node, cur_level = q.popleft()
            
            if cur_node in seen:
                continue
            seen.add(cur_node)

            if cur_level == level:
                friends_level.append(cur_node)
                continue
            
            if cur_level > level:
                continue

            for node in friends[cur_node]:
                if node not in seen:
                    q.append((node, cur_level + 1))

        if not friends_level:
            return []

        for x in friends_level:
            watched.extend(watchedVideos[x])

        watched = Counter(watched)

        watched = sorted([(val, key) for key, val in watched.items()])

        return [x for _, x in watched]