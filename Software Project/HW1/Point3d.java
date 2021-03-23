/**
 * A three-dimensional point class.
 */
public class Point3d {
    /** X coordinate of the point */
    private double xCoord;

    /** Y coordinate of the point */
    private double yCoord;

    /** Z coordinate of the point */
    private double zCoord;

    /** Constructor to initialize point to (x, y, z) value. */
    public Point3d(double x, double y, double z) {
        xCoord = x;
        yCoord = y;
        zCoord = z;
    }

    /** No-argument constructor:  defaults to a point at the origin. */
    public Point3d() {
        // Call three-argument constructor and specify the origin.
        this(0, 0, 0);
    }

    /** Compare two points for equality. */
    @Override
    public boolean equals(Object o) {
        // Check input type
        if (o instanceof Point3d){
            // Cast another object to Point3d type,
            Point3d another = (Point3d) o;
            if (xCoord == another.getX() && yCoord == another.getY() && zCoord == another.getZ()){
                return true;
            }
        }
        // if is not, it should be false
        return false;
    }

    /** Compute the straight-line distance between two points. */
    public double distanceTo(Point3d pt) {
        // Store result in variable "result"
        double result;
        result = Math.sqrt(Math.pow(xCoord-pt.getX(), 2) + Math.pow(yCoord-pt.getY(), 2) + Math.pow(zCoord-pt.getZ(), 2));
        return result;
    }

    /** Return the X coordinate of the point. */
    public double getX() {
        return xCoord;
    }

    /** Return the Y coordinate of the point. */
    public double getY() {
        return yCoord;
    }

    /** Return the Z coordinate of the point. */
    public double getZ() {
        return zCoord;
    }

    /** Set the X coordinate of the point. */
    public void setX(double val) {
        xCoord = val;
    }

    /** Set the Y coordinate of the point. */
    public void setY(double val) {
        yCoord = val;
    }

    /** Set the Z coordinate of the point. */
    public void setZ(double val) {
        zCoord = val;
    }
}
