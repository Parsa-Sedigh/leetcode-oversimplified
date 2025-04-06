When trying to find the starting node of the cycle, the exact meeting point of slow and fast is crucial. If the fast pointer starts at
head.Next, the pointers may meet at a different node within the cycle compared to when they both start at head.
This difference can lead to incorrect identification of the cycle's entry point. So both fast and slow pointers
should be initialized at head.