# fashion neutrality trends on the runway

## about this project

i started this project in november of 2025 because i kept seeing people online talking about how fashion has been “getting more neutral” over the past decade, fewer bold colors, more beige, gray, black, and muted tones, and how that might connect to things like minimalism, sustainability, social media aesthetics, economic uncertainty, or even how we consume trends now...

i wanted to see if that idea actually shows up in the data, so this project looks at runway images over time to answer:

**are runway collections becoming more neutral in color over time?**

to explore that, i use computer vision and unsupervised learning to extract dominant color palettes from runway looks and measure how “neutral” each look is based on color chroma. then i aggregate those measurements by year and visualize how they change over time.

i used the internet archive "vogue runway" dataset.

right now this repo contains the early foundation of that pipeline, very much a work in progress

---

## current status 

so far i have:

- set up the project environment and repo structure  
- loaded runway metadata and sampled looks evenly by year  
- built a baseline image preprocessing pipeline  
- implemented k-means color palette extraction  
- computed initial neutrality metrics per image  

results at this stage are preliminary and noisy, mostly because the sample size is still small and the masking is intentionally simple. the goal for now is to get the pipeline working end-to-end before making it more robust.

## results

i sucessfully analyzed how image color properties have changed over time using two main metrics: mean chroma (overall color intensity) and neutral color share (how much of an image is composed of near-gray tones). together, these give a pretty good picture of how visually “loud” or “muted” digital imagery is in a given year.

the main trend is surprisingly clean.

from about **2013 to 2015**, mean chroma drops while neutral share rises — images become more muted and minimalist. starting around **2016**, that trend reverses hard. mean chroma climbs steadily and peaks around **2019–2020**, while neutral share falls at the same time. this suggests a broad shift toward much more colorful, high-contrast visual styles in the late 2010s...

after 2020, things get messy. chroma stays high through 2021–2022 but becomes more unstable, and in **2023 there’s a sharp drop in mean chroma** paired with a rebound in neutral share. this lines up with what a lot of people anecdotally feel — that visual culture might be pulling back from the hyper-saturated look of the late 2010s.

i’d really like to extend this analysis through **2024 and 2025** once more data is available to see if this downward shift continues. unfortuantely, the dataset i used does not have much at all for 2024, so i might rerun with a different data set in the next iteration. if it does, it would suggest we’re entering a new aesthetic phase.... 

i also note that mean chroma and neutral share move almost perfectly in opposite directions across time, which is exactly what you’d expect if the metrics are actually capturing real visual change rather than noise

## next steps

future work will: 

- quantify the relationship between mean chroma and neutral share (correlation + regression)
- formally test whether the 2015 → 2020 increase in chroma is statistically significant
- align the visual trends with external events, including major cultural or political shifts, to explore whether large-scale social context might influence aesthetic direction
- expand the dataset into **2024–2025** to test whether the recent decline is the start of a new long-term trend 


---

## setup

install dependencies with:

```bash
pip install -r requirements.txt

