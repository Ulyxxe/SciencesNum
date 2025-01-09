# Simulation of the Einstein Effect for Two Recent Experiments

This project simulates the **Einstein effect** (gravitational redshift) for two real-world experiments:

1. **Galileo satellites** launched into incorrect orbits (2018)
2. **Star S2** orbiting the supermassive black hole at the center of the Galaxy (2018 results)

The goal is to compare the theoretical predictions of the Einstein effect with real-world measurement results.

---

## 1. What is the Einstein Effect?

The Einstein effect, or **gravitational redshift**, refers to the change in frequency of light or signals due to gravity. When a signal leaves a strong gravitational field, it loses energy, which causes its frequency to decrease.

### Example analogy:
- Imagine throwing a ball upwards. The stronger the gravity, the more energy the ball loses as it rises.
- Similarly, when light or a signal escapes from a region with strong gravity, it loses energy, resulting in a lower frequency.

In both experiments, we measure how much the frequency of light or signals changes because of gravity, and we compare these measurements to theoretical predictions.

---

## 2. Simulation Steps

### **Experiment 1: Galileo Satellites in Incorrect Orbits**

#### Context:
In 2018, two Galileo GPS satellites were accidentally placed into **elliptical orbits** instead of circular ones. This provided a unique opportunity to observe how their signals were affected by the varying gravitational field of Earth as the satellites moved closer to and farther from Earth.

#### Simulation:
1. Compute the gravitational redshift at the **closest point (perigee)** and the **farthest point (apogee)** of the satellite's orbit.
2. Use the gravitational potential formula:

   $$
   U = - \frac{GM}{r}
   $$

   where:
   - \( G \) is the gravitational constant
   - \( M \) is the mass of Earth
   - \( r \) is the distance from the satellite to Earth

3. Calculate the frequency shift using:

   $$  \frac{\Delta f}{f} = \frac{\Delta U}{c^2} $$

   where \( c \) is the speed of light.

4. Compare the theoretical predictions with the measured data from 2018.

### **Experiment 2: Star S2 Orbiting a Black Hole**

#### Context:
The star **S2** orbits very close to the supermassive black hole **Sagittarius A*** at the center of our galaxy. In 2018, scientists observed the gravitational redshift of light from S2 as it passed near the black hole (at its closest approach, called **peribothron**).

#### Simulation:
1. Model the orbit of S2 around Sagittarius A* using elliptical parameters.
2. Compute the gravitational potential due to the black hole's mass.
3. Calculate the redshift at the closest point (**peribothron**) and the farthest point (**apobothron**) of S2’s orbit.
4. Compare the theoretical predictions with the measurements published in 2018.

---

## 3. Results Comparison

The results include:
- **Gravitational redshift at perigee and apogee** for Galileo satellites.
- **Gravitational redshift at peribothron and apobothron** for the star S2.
- A comparison of theoretical predictions with actual measurements.

---


## 4. Conclusion

This project demonstrates the universal applicability of Einstein’s theory of general relativity, from Earth’s orbit to the environment near a supermassive black hole. By simulating these two real-world cases, we can see how well theoretical predictions match experimental data, highlighting the precision of general relativity in explaining gravitational phenomena.

---

## 5. References
- ESA Galileo Satellite Experiment (2018)
- GRAVITY Collaboration: Observation of S2 near Sagittarius A* (2018)
- Einstein's General Theory of Relativity
