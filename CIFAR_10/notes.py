"""
xnor.0.weight (192, 3, 5, 5)
xnor.3.conv.weight (160, 192, 1, 1)
xnor.4.conv.weight (96, 160, 1, 1)
xnor.6.conv.weight (192, 96, 5, 5)
xnor.7.conv.weight (192, 192, 1, 1)
xnor.8.conv.weight (192, 192, 1, 1)
xnor.10.conv.weight (192, 192, 3, 3)
xnor.11.conv.weight (192, 192, 1, 1)
xnor.13.weight (10, 192, 1, 1)
"""

1. Why weights are more important than bias?
    weights are multiplications
    weights handle with inputs while bias are always the same for all data

    1      2      3     4     5     6     7      8     9
Max 1.02%  0.89%  0.67% 0.26% 0.53% 0.22% 0.05%  0.12% 0.83%
Avg 0.23%  0.30%  0.21% 0.03% 0.12% 0.03% 0.001% 0.02% 0.04%

one   [conv1, 1] [conv2, 0] [conv3, 0] [con4, 0] 
point [conv1, 984, 0.0683] [conv2, 2481, 0.0807] [conv3, 167, 0.0109 ] [conv4, 11*96, 0.0023] [conv7, 0] [conv8, 0] [conv9, 5, 0.0026]

Float
