# PySpline
A collection of computational curves in python.
This is an upgraded version of computational curves for a previous project.

Previously Trigonometry and long equations were used to compute points in the spline like:
``` python
ptx = 0.5 * ( (2 * p1.x) + (-1 * p0.x + p2.x) * t + (2 * p0.x - 5 * p1.x + 4 * p2.x - p3.x) * t2 + ( -1 * p0.x + 3 * p1.x - 3 * p2.x + p3.x )* t3 )
``` 
Now use vectors and matrices to compute the vector 
``` python
point = 0.5 * QVector4D(1.0, t, t*t, t*t*t) * M * P    
```

## Libraries
- PyQt5

