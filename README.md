# csds_344_project1
Traffic lights

This simulation uses traffic lights and a four-way crossing visual to demonstrate the way in which vehicular and pedestrian traffic are managed safely. This includes moving pedestrian traffic appropriately while allowing other movable vehicle traffic in other directions. You can safely pass right, left and through pass vehicle traffic at the intersection. 

Rules: 
1. lights facing N/S and E/W are pairs. Each pair has the same behavior. (reword)
2. When north/south facing lights are green or yellow, east/west facing lights should be red (and vice versa)
3. Transition of colors should be green for 5 seconds then yellow for 3 seconds then red for 5 seconds then back to green

4. Anticipate all secure and unsecure states and implement mechanisms (traffic light sequences) to ensure a secure state

#our part 
Secure States (only thinking about vehicles going straight or right, no pedestrians)
1. all lights are red. No cars are in the intersection. Pedestrians on N/S and E/W can cross and vibe. 
2. Only N/S lights are red and cars are stopped. E/W are green and cars are moving. The cars on the E/W side can go straight or right. Pedestrians can't cross anywhere. 
3. Only E/W lights are red and cars are stopped. N/S are green and cars are moving. The cars on the N/S side can go straight or right. 
4. Only N/S lights are red. E/W are yellow and car traffic is slow/stopping. The cars on the E/W side can go right or straight. 
5. Only E/W lights are red. N/S are yellow and car traffic is slow/stopping. 

#confirm with Prof if left turns need to be accounted for
6. N/S lights only allow for left turns. E/W are red. Cars on N/S can only turn left.
7. E/W lights only allow for left turns. N/A are red. Cars on E/W can only turn left.

Unsecure States
1. E/W pedestrians risk being run over if they cross N/S lights being green or yellow because of cars turning right on green. 
2. N/S pedestrians risk being run over if they cross E/W lights being green or yellow because of cars turning right on green. 
3. Pedestrians try to cross diagonally. 
4. Cars turn right on red, there may be pedestrians crossing in the area that they are allowed in. 