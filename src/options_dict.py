def mov_linear_frente(msg, instance):
    msg.linear.x = instance.get_vel_linear()
    msg.linear.z = 0

def mov_linear_tras(msg, instance):
    msg.linear.x = -instance.get_vel_linear()
    msg.linear.z = 0

def mov_angular_anti(msg, instance):
    msg.linear.x = 0
    msg.angular.z = instance.get_vel_angular()

def mov_angular_hor(msg, instance):
    msg.linear.x = 0
    msg.angular.z = -instance.get_vel_angular()

def mov_linear_frente_giro_anti(msg, instance):
    msg.linear.x = instance.get_vel_linear()
    msg.angular.z = instance.get_vel_angular()

def mov_linear_tras_giro_anti(msg, instance):
    msg.linear.x = -instance.get_vel_linear()
    msg.angular.z = -instance.get_vel_angular()

def mov_linear_frente_giro_hor(msg, instance):
    msg.linear.x = instance.get_vel_linear()
    msg.angular.z = -instance.get_vel_angular()

def mov_linear_tras_giro_hor(msg, instance):
    msg.linear.x = -instance.get_vel_linear()
    msg.angular.z = instance.get_vel_angular()

def parado(msg, instance):
    msg.linear.x = 0
    msg.angular.z = 0

def inc_vel_linear(msg, instance):
    instance.set_vel_linear(instance.get_vel_linear() + instance.get_vel_linear()/100*20)
    print(f"Linear Velocity: {instance.get_vel_linear()}")

def dec_vel_linear(msg, instance):
    instance.set_vel_linear(instance.get_vel_linear() - instance.get_vel_linear()/100*20)
    print(f"Linear Velocity: {instance.get_vel_linear()}")

def inc_vel_angular(msg, instance):
    instance.set_vel_angular(instance.get_vel_angular() + instance.get_vel_angular()/100*20)
    print(f"Angular Velocity: {instance.get_vel_angular()}")

def dec_vel_angular(msg, instance):
    instance.set_vel_angular(instance.get_vel_angular() - instance.get_vel_angular()/100*20)
    print(f"Angular Velocity: {instance.get_vel_angular()}")

def fecha_no(msg, instance):
    instance.close_app()

option_dict = {
    "w": ["Movimento linear para frente", mov_linear_frente],
    "x": ["Movimento linear para trás", mov_linear_tras],
    "a": ["Movimento angular anti-horário", mov_angular_anti],
    "d": ["Movimento angular horário", mov_angular_hor],
    "q": ["Movimento linear para frente com giro anti-horário", mov_linear_frente_giro_anti],
    "z": ["Movimento linear para trás com giro anti-horário", mov_linear_tras_giro_anti],
    "e": ["Movimento linear para frente com giro horário", mov_linear_frente_giro_hor],
    "c": ["Movimento linear para trás com giro horário", mov_linear_tras_giro_hor],
    "s": ["Parado", parado],
    "1": ["Incrementa a velocidade linear", inc_vel_linear],
    "2": ["Decrementa a velocidade linear", dec_vel_linear],
    "3": ["Incrementa a velocidade angular", inc_vel_angular],
    "4": ["Decrementa a velocidade angular", dec_vel_angular],
    "p": ["Fecha o nó", fecha_no],
}
