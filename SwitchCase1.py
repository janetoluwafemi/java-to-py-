
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
prompt2 ="""
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
1 -> Alarm clock
2 -> Clock settings
3 -> Date setting
4 -> Stopwatch
5 -> Countdown timer
6 -> Auto update of date and time
7 -> Back
""";
print(prompt)
option = int(input("press between option 1 - 13"))
match option:
	case 1:
		print(" ")
		option1 = int(input(" " + prompt2))
		match option1:
			case 1:
				print("Search")
				
			case 2:
				print("Service Nos.")
				
			case 3: 
				print("Add name")
				
			case 4: 
				print("Erase")
				
			case 5: 
				print("Edit")
				
			case 6: 
				print("Search")
				
			case 7: 
				print("Service Nos.")

			case 8:
				print("Options")
				option8 = int(input(" " + a))
				match option8:
					case 1: print("Type of view")
					case 2: print("Memory status")
					case 3: print(print("" + prompt2))
				
		
			case 9: 
				print("Erase")
			
			case 10: 
				print("Edit")
			
			default: 
				print("Wrong input")
			
                        

      
    		print("Messages")
		option1 = int(input(" " + prompt3))
		match option2:
			case 1:
				print("Write messages")
                       	
                	case 2:
                        	print("Inbox")
                    
                	case 3:
                        	print("Outbox")
                       
                	case 4:
                        	print("Picture messages")
                    
                	case 5:
                      		print("Template")
                      
                	case 6:
                        	print("Smileys")
                       
                	case 7:
                        	print("Message setting")
                       	
			
				match option7:
				option1 = int(input(" " + b))
					case 1: 

						match option7a:
						option1 = int(input(" " + b1))
							case 1: 
								print("Message center number") 
						
							case 2: 
								print("Message sent as") 
						
							case 3: 
								print("Message validity") 
						
					case 2:
						match option7b:
						option1 = int(input(" " + b2))

							case 1: 
								print("Delivery report") 
						
							case 2: 
								print("Reply via same centre") 
					
							case 3: 
								print("Character support") 

                	case 8: 
				print("Info service")
                      
                	case 9:
                       	 	print("Voice mailbox number")
                       
                	case 10:
                       		print("Service command editor")
                       
                	default:
                        	print("Go back")
                       
    	
			
       			case 3:
              			print("Chat")
				option1 = int(input(" " + b))

      			case 4: print("Call register")
				option1 = int(input(" " + b))
					match option4:
						case 1: 
							print("Missed calls")
			
						case 2: 
							print("Recevied calls")
			
						case 3: 
							print("Dialled number")
		
						case 4: 
							print("Erase recent call list")
			
						case 5: 
							print("Show call duration")

					match option5:
						case 1: 
							print("Last call duration")
				
						case 2: 
							print("All calls' duration")
				
						case 3: 
							print("Recieved calls' duration")
				
						case 4: 
							print("Dialled calls' duration")
				
						case 5: 
							print("Clear timers")
			
				
			
						case 6: 
							print("Show call costs")
			
					match option6:
							case 1: 
								print("Last duration")
				
			case 2: 
				print("All calls' cost")
				
			case 3: 
				print("Clear counter")
		
				
		case 7: 
			print("Call cost setting")
			match option7:
				case 1: 
					print("Call cost limit")
					
				case 2: 
					print("Show costs in")
					
				
			
		case 8: 
			print("Prepaid credit")
				
        	
    case 5:
		print("Tones")
		match option5a:
		option = int(input(" " + prompt5)
			case 1: 
				print("Ringing tone")
			
			case 2: 
				print("Ringing volume")
			
			case 3: 
				print("Incoming call alert")
			
			case 4: 
				print("Composer")
			
			case 5: 
				print("Message alert tone")
			
			case 6: 
				print("Keypad tones")
			
			case 7: 
				print("Warning and game tone")
			
			case 8: 
				print("Vibrating alert")
			
			case 9: 
				print("Screen saver")
		
    case 6:
           print("Settings")
		
	match option6:
		case 1: 
			print("Call settings")
							
			match option6a:
			option = int(input(" " + call)
				case 1: 
					print("Automatic redial")
					
				case 2: 
					print("Speed dialling")
					
				case 3: 
					print("Call waiting options")
					
				case 4: 
					print("Own number sending")
					
				case 5: 
					print("Phone line in use")
					
				case 6: 
					print("Automatic answer")
				
		case 2: 
			print("Phone settings")
			match option3:
			option = int(input(" " + Phone)
				case 1: 
					print("Language")
					
				case 2: 
					print("Cell info display")
					
				case 3: 
					print("Welcome note")
					
				case 4: 
					print("Network selection")
						
				case 5: 
					print("Lights")
						
				case 6: 
					print("Confirm SIM service")
			
		case 3: 
			print("Security settings");
			match option3:
			option = int(input("" + setting)	
				case 1: 
					print("PIN code request")
					
				case 2: 
					print("Call info display")
					
				case 3: 
					print("Fixed dialling")
					
				case 4: 
					print("Closed user group")
					
				case 5: 
					print("Phone security")
					
				case 6: 
					print("Change access codes")
					
				
		case 4: print("Restore factory settings")
			
			
             	
		
      case 7:
             print("Call divert")
            

     case 8:
             print("Games")
      

    case 9:
            print("Calculator")
         

     case 10:
             print("Reminder")
            

    case 11:
        	print("Clock")			
		match option11a:
		option = int(input("" + prompt6)
			case 1: 
				print("Alarm clock")
				
			case 2: 
				print("Clock settings")
			
			case 3: 
				print("Date setting")
			
			case 4: 
				print("Stopwatch")
			
			case 5: 
				print("Countdown timer")
			
			case 6: 
				print("Auto update of date and time")
						

     case 12:
              print("Profiles")
              

     case 13:
              print("SIM services")
            

     default:
              print("Invalid option")
              
	