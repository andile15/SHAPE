# Plot the shape of a nucleus

import numpy as np
import matplotlib.pyplot as plt

plt.ioff()

# Define nuclues
r0 = 1.2

# User input
while True:
    Z = input("Enter atomic number Z (default: 10): ").strip()
    if not Z:
        Z = 10
        break
    try:
        Z = int(Z)
        break
    except ValueError:
        print("\nPlease enter atomic number Z or press Enter for default")
    
    
    
while True:
    A = input("Enter atomic mass number A (default: 20): ").strip()
    if not A:
        A = 20
        break
    try:
        A = int(A)
        break
    except ValueError:
        print("\nPlease enter atomic mass A or press Enter for default")   
    
 
    
while True:
    Qs = input("Enter spectroscopic quadrupole moment Qs (defualt: 0): ").strip()
    if not Qs:
        Qs = 0
        break
    try:
        Qs = float(Qs)
        break
    except ValueError:
        print("\nPlease enter Qs value or press Enter for default")  



while True:
    gamma = input("Enter gamma value (default: 0): ").strip()
    if not gamma:
        gamma = 0
        break
    try:
        gamma = float(gamma)
        gamma = np.radians(gamma)
        break
    except ValueError:
        print("\nPlease enter gamma (y) value or press Enter for default") 

# Calculate average radius
R_ave = r0*pow(A, 1/3)      # in (fm)
R_ave2 = 0.0144*pow(A, 2/3) # convert to barns (b)

# Deformation paramteters

Q0 = -(7/2)*Qs  # calculates intrinsic quadrupole moment 
beta = (np.sqrt(5*np.pi)/3)*(Q0/(Z*R_ave2))



# Prints calculated parameters
'''
print("")
print("==================================")
print("  Q0 = ", Q0)
print("beta = ", beta)
print("==================================")
'''

# Calculating Surface
# Define angles
theta = np.linspace(0, np.pi, 31)
phi = np.linspace(0, 2*np.pi, 31)
(Theta, Phi) = np.meshgrid(theta, phi)

Rsurf1 = R_ave*(1+beta*np.sqrt((5/(4*np.pi)))*np.cos(gamma-((2*np.pi*1)/3)))
Rsurf2 = R_ave*(1+beta*np.sqrt((5/(4*np.pi)))*np.cos(gamma-((2*np.pi*2)/3)))
Rsurf3 = R_ave*(1+beta*np.sqrt((5/(4*np.pi)))*np.cos(gamma-((2*np.pi*3)/3)))

# Cartesian Cooridnates
x = Rsurf1*np.sin(Theta)*np.cos(Phi)
y = Rsurf2*np.sin(Theta)*np.sin(Phi)
z = Rsurf3*np.cos(Theta)

# Axis limits 
xmax = np.max(x)
ymax = np.max(y)
zmax = np.max(z)

zmin = np.min(z)
axMax = np.max(np.array([xmax,ymax,zmax]))/2

# Plot surface
fig = plt.figure(
                figsize=(5,5),
                edgecolor='black',
                linewidth=3,
                frameon=False,
                dpi=300
                )

ax = fig.add_subplot((111), projection='3d')

ax.plot_surface(
                x, y, z, 
                rstride=1, 
                cstride=1, 
                cmap=plt.get_cmap('viridis'),
                linewidth=0.2,
                edgecolors='k',
                alpha=1
                )



ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

ax.set_facecolor('white')
ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.w_zaxis.line.set_visible(False)

ax.xaxis.pane.set_edgecolor('r')
ax.yaxis.pane.set_edgecolor('w')
ax.zaxis.pane.set_edgecolor('w')

while True:
    try:
        grid_ = input("Display with grid and axes (default: off):[on/off] ").lower().strip()
        
        # Default value
        if not grid_:
            grid_ = str("off")
            fig.set_figwidth(2)
            fig.set_figheight(2)
        
            ax.grid(False) # Show Grid
            ax.axis('off') # Hide the axes
            
            ax.set_xlim3d(-axMax-0.5,axMax+0.5)
            ax.set_ylim3d(-axMax-0.5,axMax+0.5)
            
            if Qs<0:
                ax.set_zlim3d(-axMax-0.5,axMax+0.5)
            elif Qs==0:
                ax.set_zlim3d(-axMax-0.5,axMax+0.5)
            else:
                ax.set_zlim3d(zmin,-zmin)
        
        
            ax.set_box_aspect((1,1,1))
                    
            break
        
        # Set grid and axes on
        if grid_ == 'on':
            
            ax.grid(True) # Show Grid
            ax.axis('on') # Hide the axes
            
            fig.set_figwidth(8)
            fig.set_figheight(8)
            
            fig.set_dpi(100)
            
            ax.set_xlim3d(-axMax-5,axMax+5)
            ax.set_ylim3d(-axMax-5,axMax+5)
            ax.set_zlim3d(-axMax-5,axMax+5)
            
            ax.contour(x,y,z, zdir="x", offset=-axMax-5, cmap="viridis")
            ax.contour(x,y,z, zdir="y", offset=axMax+5, cmap="viridis")
            ax.contour(x,y,z, zdir="z", offset=-axMax-5, cmap="viridis")
            
            ax.set_box_aspect((1,1,1))
    
            ax.set_xlabel('$x$')
            ax.set_ylabel('$y$')
            ax.set_zlabel('$z$')
            
            break
        
        # Set grid and axes on
        elif grid_ == 'off':        
            
            fig.set_figwidth(2)
            fig.set_figheight(2)
            
            ax.grid(False) # Show Grid
            ax.axis('off') # Hide the axes
            
            ax.set_xlim3d(-axMax-0.5,axMax+0.5)
            ax.set_ylim3d(-axMax-0.5,axMax+0.5)
            
            if Qs<0:
                ax.set_zlim3d(-axMax-0.5,axMax+0.5)
            elif Qs==0:
                ax.set_zlim3d(-axMax-0.5,axMax+0.5)
            else:
                ax.set_zlim3d(zmin,-zmin)
            
            
            ax.set_box_aspect((1,1,1))
                    
            break
        
        else:
            raise ValueError("Invalid input. Please type 'on' or 'off' or press Enter")
            
    except ValueError as e:
        print(f"{e}")
            
        
plt.show()       

