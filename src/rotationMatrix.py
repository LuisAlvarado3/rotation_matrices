from math import radians, cos, sin

class RotationMatrix:
    def __init__(self, angle_x_y_z = (0.0, 0.0, 0.0) ) -> None:
        self.alfa_x_radians  = radians( angle_x_y_z[0] )
        self.betha_y_radians = radians( angle_x_y_z[1] )
        self.theta_z_radians = radians( angle_x_y_z[2] )
        self.MATRIX = dict()
        self.calculate_matrix()
        
    def calculate_matrix( self ) -> None:
        self.MATRIX[ "ALFA" ] = (
            ( 1.0,           0.0           ,            0.0            ),
            ( 0.0, cos(self.alfa_x_radians), -sin(self.alfa_x_radians) ),
            ( 0.0, sin(self.alfa_x_radians),  cos(self.alfa_x_radians) )
        )
        self.MATRIX[ "BETA" ] = (
            (  cos(self.betha_y_radians), 0.0, sin(self.betha_y_radians) ),
            (            0.0            , 1.0,          0.0              ),
            ( -sin(self.betha_y_radians), 0.0, cos(self.betha_y_radians) )
        )
        self.MATRIX[ "THETA" ] = (
            ( cos(self.theta_z_radians), -sin(self.theta_z_radians), 0.0 ),
            ( sin(self.theta_z_radians),  cos(self.theta_z_radians), 0.0 ),
            (            0.0           ,             0.0           , 1.0 )
        )
