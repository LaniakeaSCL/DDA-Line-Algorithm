# DDA Line Algorithm in Python

This repository contains a simple implementation of the **Digital Differential Analyzer (DDA) line algorithm** in Python. The algorithm generates all the intermediate points of a line between two given coordinates and prints them continuously until the line reaches the endpoint.

## Features
- Takes four integer inputs: `x1`, `y1`, `x2`, `y2`.
- Calculates all intermediate coordinates along the line using the DDA algorithm.
- Prints each coordinate point until the line reaches the destination.

## How It Works
The **DDA (Digital Differential Analyzer) algorithm** works by:
1. Calculating the difference in `x` and `y` (`dx`, `dy`) between the start and end points.
2. Determining the number of steps required based on the greater of `dx` or `dy`.
3. Incrementing `x` and `y` values in small steps and rounding them to get integer coordinates.
4. Printing each point until the line reaches the endpoint `(x2, y2)`.
