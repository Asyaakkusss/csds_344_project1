# csds_344_project1
Traffic lights

This simulation uses traffic lights and a four-way crossing visual to demonstrate the way in which vehicular and pedestrian traffic are managed safely. This includes moving pedestrian traffic appropriately while allowing other movable vehicle traffic in other directions. You can safely pass right, left and through pass vehicle traffic at the intersection. 

Rules: 
<ol>
<li> lights facing N/S and E/W are pairs. Each pair has the same behavior. (reword) </li>
<li> When north/south facing lights are green or yellow, east/west facing lights should be red (and vice versa) </li>
<li>Transition of colors should be green for 5 seconds then yellow for 3 seconds then red for 5 seconds then back to green</li>
<li>Anticipate all secure and unsecure states and implement mechanisms (traffic light sequences) to ensure a secure state</li>
</ol>

<h3>our part</h3>
<h2>Secure States (only thinking about vehicles going straight or right, no pedestrians)</h2>
<ol>
<li> all lights are red. No cars are in the intersection. Pedestrians on N/S and E/W can cross and vibe. </li> 
<li>Only N/S lights are red and cars are stopped. E/W are green and cars are moving. The cars on the E/W side can go straight or right. Pedestrians can't cross anywhere. </li>
<li>Only E/W lights are red and cars are stopped. N/S are green and cars are moving. The cars on the N/S side can go straight or right. </li>
<li> Only N/S lights are red. E/W are yellow and car traffic is slow/stopping. The cars on the E/W side can go right or straight. </li>
<li> Only E/W lights are red. N/S are yellow and car traffic is slow/stopping. </li>

#confirm with Prof if left turns need to be accounted for
<li> N/S lights only allow for left turns. E/W are red. Cars on N/S can only turn left.</li>
<li>E/W lights only allow for left turns. N/A are red. Cars on E/W can only turn left.</li>

</ol>

<h2>Unsecure States</h2>
<ol>
<li> E/W pedestrians risk being run over if they cross N/S lights being green or yellow because of cars turning right. </li>
<li> N/S pedestrians risk being run over if they cross E/W lights being green or yellow because of cars turning right. </li>
<li> Pedestrians try to cross diagonally.</li>
<li>Cars turn right on red, there may be pedestrians crossing. </li>
</ol>