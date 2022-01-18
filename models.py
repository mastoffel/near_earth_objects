"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.
"""

from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(self, designation = '', name = None, diameter = float('nan'), hazardous = False, approaches = []):
        """Create a new `NearEarthObject`.

        :param designation (str): Designation, a unique identifier.
        :param name (str): Name, if present.
        :param diameter (float): Diameter in km.
        :param hazardous(boolean): Is NEO deemed potentially hazardous.
        :param approaches: List of close approaches.
        """

        self.designation = designation
        if not name:
            self.name = None
        else:
            self.name = name
        if not diameter:
            self.diameter = float('nan')
        else:
            self.diameter = float(diameter)
        if hazardous == 'N' or not hazardous:
            self.hazardous = False
        else:
            self.hazardous = True

        # Create an empty initial collection of linked approaches.
        self.approaches = approaches

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""

        if self.name:
            fullname = f"{self.designation} ({self.name})"
        else:
            fullname = self.designation
        return fullname

    def __str__(self):
        """Return `str(self)`."""
        if self.hazardous:
            haz = "is"
        else:
            haz = "is not"
        return f"Near-earth object {self.fullname} has a diameter {self.diameter} km and {haz} potentially hazardous"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, designation = '', time = None, distance = 0.0, velocity = 0.0, neo = None):
        """Create a new `CloseApproach`.

        :param designation: The NEO designation.
        :param time: Approach data and time, format yyyy-mm-dd hh:mm.
        :param distance: Distance in au
        :param velocity: Velocity in km/s
        :param neo: NearEarthObject associated with CloseApproach.
        """
 
        self._designation = designation
        self.time = cd_to_datetime(time)  
        self.distance = float(distance)
        self.velocity = float(velocity)

        # Create an attribute for the referenced NEO, originally None.
        self.neo = neo

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time."""
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        return f"On {self.time_str}, {self.neo.fullname} approaches Earth at a distance of {self.distance:.2f} au and a velocity of {self.velocity:.2f}."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")

    def serialize_flat(self):
        """Serializes approach object into flat dictionary."""
        serial_ca = {
            'datetime_utc': datetime_to_str(self.time),
            'distance_au': float(self.distance),
            'velocity_km_s': float(self.velocity),
            'designation': str(self._designation),
            'name': str(self.neo.name) if self.neo.name is not None else '',
            'diameter_km': float(self.neo.diameter),
            'potentially_hazardous': self.neo.hazardous
        }
        return serial_ca
    
    def serialize_nested(self):
        """Serializes approach object into nested dictionary for json output."""
        nested_serial_ca = {
            'datetime_utc': datetime_to_str(self.time),
            'distance_au': float(self.distance),
            'velocity_km_s': float(self.velocity),
            'neo': {
                'designation': str(self.neo.designation),
                'name': str(self.neo.name) if self.neo.name is not None else '',
                'diameter_km': float(self.neo.diameter),
                'potentially_hazardous': self.neo.hazardous
            }
        }
        return nested_serial_ca