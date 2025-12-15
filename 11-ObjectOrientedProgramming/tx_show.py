import tv
def main():
   # object creation
   tele = tv.TV()

   # object usage
   tele.show_status()
   tele.turn_on()
   tele.show_status()
   tele.set_channel(5)
   tele.show_status()
   tele.turn_off()
   tele.show_status()


if __name__ == "__main__":
   main() 