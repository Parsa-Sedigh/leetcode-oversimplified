### About sliding window(optimal):
Why `l = max(l, mp[s[r]] + 1)`?

This is because we're not deleting anything from mp in case there's a duplicate.
When there's a dup, there are 2 cases we need to deal:
1. dup is behind l(mp[sr] + 1 <= l). Meaning it's already outside our window, so we just preserve l where it is
2. dup is after l(between l and r - (mp[sr] + 1 > l)). We need to move l after where the dup exists(mp[s[r]] + 1), since our window
becomes invalid.

Side note: If l is the dup one(with r), it means the window becomes invalid, we just need to move l by one index. So in `max(mp[s[r]] + 1, l)`,
mp[s[r] + 1] is the max and therefore, we move l forward.