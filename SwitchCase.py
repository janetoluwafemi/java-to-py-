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
	