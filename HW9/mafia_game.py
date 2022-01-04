# MAFIA

class EventsOfTheNight:
    
    def __init__(self) -> None:
        self.events = []
    
    def add_event(self, event):
        self.events.append(event)
   
    def delete_events(self):
        self.events.clear()

    def get_events(self):
        return " ".join(self.events)


class Voting:#tools

    @staticmethod
    def count_the_votes(band, list_of_live):
        
        while True:
            list_votes = []
            rez = {k:0 for k in list_of_live}
            for player in list_of_live:
                if isinstance(player, band):
                    while True:
                        vote = player.get_vote(list_of_live)
                        if vote in list_of_live:
                            rez[vote] += 1
                            break
            max_val = max(rez.values())
            final_rez = {k:v for k, v in rez.items() if v == max_val}
            if len(final_rez) == 1:
               for k in final_rez:
                   print(f"Point to {k}.")
                   return k
            else:
                print("Try again.")


class Master:

    def __init__(self) -> None:
        
        self.set_list_of_live([])
        self.set_list_of_died([])
        self.set_list_of_prison([])
        self.list_events = EventsOfTheNight()
    
    def set_list_of_live(self, list_of_live):
        self.__list_of_live = list_of_live

    def set_list_of_died(self, list_of_died):
        self.__list_of_died = list_of_died 

    def set_list_of_prison(self, list_of_prison):
        self.__list_of_prison = list_of_prison 

    def add_item_in_list_of_live(self, player):
        self.__list_of_live.append(player)

    def add_item_in_list_of_died(self, player):
        self.__list_of_died.append(player) 

    def add_item_in_list_of_prison(self, player):
        self.__list_of_prison.append(player)

    def get_list_of_live(self):
        return self.__list_of_live

    def get_list_of_died(self):
        return self.__list_of_died

    def get_list_of_prison(self):
        return self.__list_of_prison
    
    def get_extra_list(self):
        extra_list = list(self.list_of_live)
        if len(self.list_of_died) > 0:
            extra_list.append(self.list_of_died[-1])
        return extra_list

    list_of_live = property(get_list_of_live, set_list_of_live)
    list_of_died = property(get_list_of_died, set_list_of_died)
    list_of_prison = property(get_list_of_prison, set_list_of_prison)

    def announce_day(self, first_day=False):
        
        print("The day is coming. Everyone wakes up.")
        for player in self.list_of_live:
            player.sleep = False 
        if first_day:    
            print("The mafia appeared in the city!")
        else:
            events = self.list_events.get_events()
            if len(events) > 0:
                print(f"Events of the night:{events}")
                self.list_events.delete_events()
            else:
                print("It was a quiet night. Everyone stayed alive.")
        if self.end_of_the_game():
            return True
        print("Choosing a suspect...")
        suspect = Voting.count_the_votes(Player, self.list_of_live)
        if suspect.immunity == True:
            print("This player has alibi!")
        else:
            print(f"{suspect} goes to the prison.")
            self.add_item_in_list_of_prison(suspect)
            self.list_of_live.remove(suspect)
        for player in self.list_of_live:
            player.healing = False
            player.immunity = False
        if self.end_of_the_game():
            return True

    def check_end(self):
        
        num_mafia = 0
        num_peace = 0
        for player in self.list_of_live:
            if isinstance(player, Mafia):
                num_mafia += 1
            elif isinstance(player, PeacefulInhabitant):
                num_peace +=1
            if num_peace > 0 and num_mafia > 0:
                return False
        if num_mafia > 0:
            return "MAFIA"
        else:
            return "Сivilians"
            
    def end_of_the_game(self):
        
        dop_str = {Don:"Don", Commissar:"Commissar", Cutie:"Cutie", Doctor:"Doctor", PeacefulInhabitant: "Peaceful inhabitant", Mafia: "Mafia"}
        win = self.check_end()
        if win:
            print(f"The end of the game. {win} is winner!")
            print(f"Killed players:")
                        
            for player in self.list_of_died:
                print(f"{player.name} - {dop_str[type(player)]}")
            print(f"Players in prison:")
            for player in self.list_of_prison:
                print(f"{player.name} - {dop_str[type(player)]}")
            return True
  
    def announce_hight(self):
        
        print("The city falls asleep.")
        self.fall_asleep(Player)

    def wake_up(self, band):
        
        for player in self.list_of_live:
            if isinstance(player, band):
                player.sleep = False
                if band in {Cutie, Doctor, Commissar, Don}:
                    return player

    def fall_asleep(self, band):
        
        for player in self.list_of_live:
            if isinstance(player, band):
                player.sleep = True

    def show_yes(self):
        return "Master nods in agreement."

    def show_no(self):
        return "Master shakes his head to show no."

    def show_death(self):
        return "The GM crosses his arms over his chest to indicate that the player has been killed."

    def play_the_mafia_part(self):
        
        print("The mafia wakes up.")
        self.wake_up(Mafia)
        print("Mafia chooses victim...")
        victim = Mafia.killed_victim(self.list_of_live)
        self.list_events.add_event(f"Mafia killed {victim}.")
        self.list_of_live.remove(victim)
        self.add_item_in_list_of_died(victim) 
        print("The mafia falls asleep.")
        self.fall_asleep(Mafia)

    def play_the_doctor_part(self):
        
        print("The doctor wakes up.")
        player = self.wake_up(Doctor)
        save_player = player.heal(self.get_extra_list())
        if save_player in self.list_of_died:
            self.list_of_died.remove(save_player)
            self.add_item_in_list_of_live(save_player)
            self.list_events.events.pop()
        print("The doctor falls asleep.")
        self.fall_asleep(Doctor)
     
    def play_the_cutie_part(self):
        
        print("The cutie wakes up.")
        player = self.wake_up(Cutie)
        player.give_immunity(self.get_extra_list())
        print("The cutie falls asleep.")
        self.fall_asleep(Cutie)

    def play_the_don_party(self):
        
        print("Don wakes up.")
        player = self.wake_up(Don)
        print("Don checks commisar...")
        check_player = player.check_commissar(self.list_of_live)
        if isinstance(check_player,Commissar):
            print(f"{self.show_yes()} {check_player} is the commissar.")
        else:
            print(f"{self.show_no()} {check_player} isn't the commissar.")
        print("Don falls asleep.")
        self.fall_asleep(Don)

    def play_the_commissar_part(self):
        
        print("Commissar wakes up.")
        player = self.wake_up(Commissar)
        print("Commissar checks player...")
        check_player = player.check_mafia(self.get_extra_list())
        if isinstance(check_player,Mafia):
            print(f"{self.show_yes()} {check_player} is a mafia.")
        else:
            print(f"{self.show_no()} {check_player} isn't a mafia.")
        if len(self.list_of_died) > 0 and check_player in self.list_of_died:
            print(f"{self.show_death()}")
        print("Commissar falls asleep.")
        self.fall_asleep(Commissar)

    def play_game(self):
        
        self.announce_hight()
        self.wake_up(Mafia) #mafia meets
        self.announce_day(first_day=True)
        while not self.end_of_the_game():
            self.announce_hight
            if any([isinstance(player, Mafia) for player in self.list_of_live]):
                self.play_the_mafia_part()
            if any([isinstance(player, Don) for player in self.list_of_live]) and any([isinstance(player, PeacefulInhabitant) for player in self.list_of_live]):
                self.play_the_don_party()
            if any([isinstance(player, Doctor) for player in self.list_of_live]):
                self.play_the_doctor_part()
            if any([isinstance(player, Commissar) for player in self.list_of_live]):
                self.play_the_commissar_part()
            if any([isinstance(player, Cutie) for player in self.list_of_live]):
                self.play_the_cutie_part()
            if self.announce_day():
                break
        print("***END OF THE GAME***")       

class Player:

    def __init__(self, name) -> None:
        self.set_name(name)
        self.set_live(True)
        self.set_sleep(False)
        self.set_immunity(False)
        self.set_healing(False)

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name    

    def set_live(self, state_live):
        self.__live = state_live

    def set_sleep(self, state_sleep):
        self.__sleep = state_sleep

    def set_immunity(self, state_immunity):
        self.__immunity = state_immunity 
    def get_immunity(self):
        return self.__immunity

    def set_healing(self, state_healing):
        self.__healing = state_healing

    def get_vote(self, list_players):#Для данной реализации считаем, что имена - логины уникальны.
        while True:
            name = input(f"{self} chooses...")
            for player in list_players:
                if name == player.name:
                    return player
            print("Try again.")

    def __str__(self) -> str:
        return self.__name

    def choose_suspect(self, list_of_live):
        while True:
            suspect = Voting.count_the_votes(Player, list_of_live)
            if suspect.immunity == False:
                Master.add_item_in_list_of_prison(suspect)
                return suspect
    
    live = property(fset = set_live)
    sleep = property(fset=set_sleep)
    immunity = property(get_immunity, fset = set_immunity)
    healing = property(fset = set_healing)
    name = property(get_name, set_name)

class Mafia(Player):
    
    @staticmethod
    def killed_victim(list_of_live):
        victim = Voting.count_the_votes(Mafia, list_of_live)
        victim.live = False
        return victim

class Don(Mafia):

    def check_commissar(self, list_of_live):
        return self.get_vote(list_of_live)
        
class PeacefulInhabitant(Player):pass
    
class Doctor(PeacefulInhabitant):
    
    def heal(self, list_of_players):
        save_player = self.get_vote(list_of_players)
        save_player.healing = True
        return save_player

class Cutie(PeacefulInhabitant):
   
    def give_immunity(self, list_of_players):
        save_player = self.get_vote(list_of_players)
        save_player.immunity = True
        return save_player

class Commissar(PeacefulInhabitant):
    
    def check_mafia(self, list_of_players):
        return self.get_vote(list_of_players)

#Players 
master_of_game = Master()
maf1 = Don("maf1")
maf2 = Mafia("maf2")
maf3 = Mafia("maf3")
man1 = Commissar("man1")
man2 = Doctor("man2")
man3 = Cutie("man3")
man4 = PeacefulInhabitant("man4")
# set
master_of_game.add_item_in_list_of_live(maf1)
master_of_game.add_item_in_list_of_live(maf2)
master_of_game.add_item_in_list_of_live(maf3)
master_of_game.add_item_in_list_of_live(man1)
master_of_game.add_item_in_list_of_live(man2)
master_of_game.add_item_in_list_of_live(man3)
master_of_game.add_item_in_list_of_live(man4)
# Game
master_of_game.play_game()







