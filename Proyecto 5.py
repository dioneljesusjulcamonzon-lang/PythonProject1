
# CORRECTO: Notificador depende de una abstracción (ServicioMensaje)
class ServicioMensaje(ABC):
    @abstractmethod
    def enviar(self, msg): pass

class ServicioSMS(ServicioMensaje):
    def enviar(self, msg): print(f"SMS: {msg}")

class ServicioEmail(ServicioMensaje):
    def enviar(self, msg): print(f"Email: {msg}")
