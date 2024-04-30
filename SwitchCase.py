
prompt ="""
:::::::::::::::::::::::::::::::::::::::::::::::::
Nokia Phone Menu
::::::::::::::::::::::::::::::::::::::::::::::::
1 -> Phone book
2 -> Messages
3 -> Chat
4 -> Call register
5 -> Tones
6 -> Settings
7 -> Call divert
8 -> Games
9 -> Calculator
10 -> Reminder
11 -> Clock
12 -> Profiles
13 -> SIM services
14 -> Back
""";

String prompt2 ="""
Phone Book
1 -> Search
2 -> Service Nos.
3 -> Add name
4 -> Erase
5 -> Edit
6 -> Assign tone
7 -> Send b'card
8 -> Options
9 -> Speed dials
10 -> Voice tags
11 -> Back
""";
a="""
1 -> Type of view 
2 -> Memory status
3 -> Back
""";
prompt3 = """
Press
1 -> Write messages
2 -> Inbox
3 -> Outbox
4 -> Picture messages
5 -> Template
6 -> Smileys
7 -> Message setting
8 -> Info service
9 -> Voice mailbox number
10 -> Service command editor
11 -> Back
""";
b="""
1 -> Set 1
2 -> Common
3 -> Back
""";
b1="""
1 -> Message centre number
2 -> Message sent as
3 -> Message validity
4 -> Back
""";
b2="""
1 -> Delivery reports
2 -> Reply via same centre
3 -> Character support
4 -> Back
""";
c="""
1 -> Missed calls
2 -> Recevied calls
3 -> Dialled number
4 -> Erase recent call list
5 -> Show call duration
6 -> Show call costs
8 -> Prepaid credit
9 -> Back
"""; 
a5="""
1 -> Last call duration
2 -> All calls' duration
3 -> Recieved calls' duration
4 -> Dialled calls' duration
5 -> Clear timers
6 -> Back
""";
a6="""
1 -> Last duration
2 -> All calls' cost
3 -> Clear counter
4 -> Back
""";
a7="""
1 -> Call cost limit
2 -> Show costs in
3 -> Back
""";
prompt4= """
Tones
press
1 -> Ringing tone
2 -> Ringing volume
3 -> Incoming call alert
4 -> Composer
5 -> Message alert tone
6 -> Keypad tones
7 -> Warning and game tone
8 -> Vibrating alert
9 -> Screen saver
10 -> Back
"""; 
prompt5= """
press
1 -> Call settings
2 -> Phone settings
3 -> Security settings
4 -> Restore factory settings
5 -> Back
""";
call="""
1 -> Automatic redial
2 -> Speed dialling
3 -> Call waiting options
4 -> Own number sending
5 -> Phone line in use
6 -> Automatic answer
7 -> Back
""";
Phone="""
1 -> Language
2 -> Cell info display
3 -> Welcome note
4 -> Network selection
5 -> Lights
6 -> Confirm SIM service
7 -> Back
 """;
setting="""
1 -> PIN code request
2 -> Call info display
3 -> Fixed dialling
4 -> Closed user group
5 -> Phone security
6 -> Change access codes
7 -> Back
""";
prompt6= """
Clock
press
1 -> Alarm clock
2 -> Clock settings
3 -> Date setting
4 -> Stopwatch
5 -> Countdown timer
6 -> Auto update of date and time
7 -> Back
""";
option = int(input("press between option 1 - 13"))
match option:
	case 1:
		
            match option1:
		case 1:
			print("Search")
			break
		case 2:
			print("Service Nos.")
			break
		case 3: 
			print("Add name")
			break
		case 4: 
			print("Erase")
			break
		case 5: 
			print("Edit")
			break
		case 6: 
			print("Search")
			break
		case 7: 
			print("Service Nos.")
			break
		case 8: print("Options")

		match option8:
                    	case 1: 
				print("Type of view")
				break
                   	case 2: 
				print("Memory status")
				break
				
		break
		case 9: 
			print("Erase")
			break
		case 10: print("Edit")
			 break
		default: print("Wrong input")
			 break
                        

        break
    	case 2: print("Messages")
	match option2:
		case 1:
			print("Write messages")
                       	break
                case 2:
                        print("Inbox")
                        break
                case 3:
                        print("Outbox")
                        break
                case 4:
                        print("Picture messages")
                        break
                case 5:
                      	print("Template")
                        break
                case 6:
                        print("Smileys")
                        break
                case 7:
                        print("Message setting")
                        break	
			
		match option7:
			case 1: 
				print("")

				match option7a:
					case 1: 
						print("Message center number") 
						break
					case 2: 
						print("Message sent as") 
						break
					case 3: 
						print("Message validity") 
						break
					
				break
			case 2: 
				print("Common")
				
				match option7b:
					case 1: 
						print("Delivery report") 
						break
					case 2: 
						print("Reply via same centre") 
						break
					case 3: 
						print("Character support") 
						break

				break
		break	
                case 8: 
			print("Info service")
                        break
                case 9:
                        print("Voice mailbox number")
                       	break
                case 10:
                       	print("Service command editor")
                        break
                default:
                        print("Go back")
                       
                
               break		
			
       	case 3:
              		print("Chat")
               		break

      	case 4: print("Call register")
	
	match option4:
		case 1: 
			print("Missed calls")
			break
		case 2: 
			print("Recevied calls")
			break
		case 3: 
			print("Dialled number")
			break
		case 4: 
			print("Erase recent call list")
			break
		case 5: 
			print("Show call duration")

		match option5:
			case 1: 
				print("Last call duration")
				break
			case 2: 
				print("All calls' duration")
				break
			case 3: 
				print("Recieved calls' duration")
				break
			case 4: 
				print("Dialled calls' duration")
				break
			case 5: 
				print("Clear timers")
				break
				
			break
				
			
		case 6: print("Show call costs")
			
		match option6:
			case 1: 
				print("Last duration")
				break
			case 2: 
				print("All calls' cost")
				break
			case 3: 
				print("Clear counter")
				break
			
			break
				
		case 7: 
			print("Call cost setting")
			match option7:
				case 1: 
					print("Call cost limit")
					break
				case 2: 
					print("Show costs in")
					break
					
				break
			
		case 8: 
			print("Prepaid credit")
			break
				
        	 break
    case 5:
	print("Tones")
	
	match option5a:
		case 1: 
			print("Ringing tone")
			break
		case 2: 
			print("Ringing volume")
			break
		case 3: 
			print("Incoming call alert")
			break
		case 4: 
			print("Composer")
			break
		case 5: 
			print("Message alert tone")
			break
		case 6: 
			print("Keypad tones")
			break
		case 7: 
			print("Warning and game tone")
			break
		case 8: 
			print("Vibrating alert")
			break
		case 9: 
			print("Screen saver")
			break
				
        	 break
    case 6:
           print("Settings")
		
	match option6:
		case 1: 
			print("Call settings")
							
			match option6a:
				case 1: 
					print("Automatic redial")
					break
				case 2: 
					print("Speed dialling")
					break
				case 3: 
					print("Call waiting options")
					break
				case 4: 
					print("Own number sending")
					break
				case 5: 
					print("Phone line in use")
					break
				case 6: 
					print("Automatic answer")
					break
						
				break
		case 2: print("Phone settings")
			match option3:
				case 1: 
					print("Language")
					break
				case 2: 
					print("Cell info display")
					break
				case 3: print("Welcome note")
					break
					case 4: 
						print("Network selection")
						break
					case 5: 
						print("Lights")
						break
					case 6: print("Confirm SIM service")
						break
						
				break;	
		case 3: 
			print("Security settings");
			match option3:	
				case 1: 
					print("PIN code request")
					break
				case 2: 
					print("Call info display")
					break
				case 3: 
					print("Fixed dialling")
					break
				case 4: 
					print("Closed user group")
					break
				case 5: print("Phone security")
					break
				case 6: print("Change access codes")
					break
				break
		case 4: print("Restore factory settings")
			break
			
             	
		break
      case 7:
             print("Call divert")
             break

     case 8:
             print("Games")
             break

     case 9:
            print("Calculator")
            break

     case 10:
             print("Reminder")
            	break

    case 11:
        print("Clock")			
	match option11:
		case 1: print("Alarm clock")
				break
		case 2: 
			print("Clock settings")
			break
		case 3: 
			print("Date setting")
			break
		case 4: 
			print("Stopwatch")
			break
		case 5: 
			print("Countdown timer")
			break
		case 6: 
			print("Auto update of date and time")
			break
						}
               	 break

     case 12:
              print("Profiles")
              break

     case 13:
              print("SIM services")
              break

      default:
              print("Invalid option")
              break
	