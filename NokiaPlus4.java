import java.util.Scanner;

public class NokiaPlus4{
	private  Scanner scanner = new Scanner(System.in);

	public void phoneMenu(){
		System.out.println("""
		phoneMenu
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
                	""");
	inputForPhoneMenu();
	}

	public void inputForPhoneMenu(){
			int phoneMenu = scanner.nextInt();
               		switch (phoneMenu) {
				case 1: displayPhoneBookOption();
				break;
				case 2: messages();
				break;
				case 3: System.out.print("Chat");
				break;
				case 4: callRegisterOptions();
				break;
				case 5: tonesOptions();
				break;
				case 6: settingsOptions();
				break;
				case 7: System.out.print("Call divert");
				break;
				case 8: System.out.print("Games");
				break;
				case 9: System.out.print("Calculator");
				break;
				case 10: System.out.print("Reminders");
				break;
				case 11: clockOptions();
				break;
				case 12: System.out.print("Profiles");
				break;
				case 13: System.out.print("SIM services");
				break;
				case 14: System.out.print("Exit");
				break;
				
			}
	}

	public void displayPhoneBookOption(){
		System.out.println("""
		PhoneBook
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
                	""");	
		inputForPhoneBook();
	}

	public void messages(){
		System.out.println("""
		messages
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
                	""");
		inputForMessage();
	}
	


	public void callRegisterOptions(){
		System.out.println("""
		call register
		1 -> Missed calls
		2 -> Recevied calls
		3 -> Dialled number
		4 -> Erase recent call list
		5 -> Show call duration
		6 -> Show call costs
		7 -> Call cost setting
		8 -> Prepaid credit
		9 -> Back
		""");
	inputForCallRegister();
	}


	public void tonesOptions(){
		System.out.println("""
		tones
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
		""");
	inputForTonesOptions();
	}
		
	public void settingsOptions(){
		System.out.println("""
		settings
		1 -> Call settings
                2 -> Phone settings
                3 -> Security settings
                4 -> Restore factory settings
		5 -> Back
		""");
	inputForSettingsOptions();
	}

	public void clockOptions(){
		System.out.println("""
		clock
		1 -> Alarm clock
                2 -> Clock settings
                3 -> Date setting
                4 -> Stopwatch
                5 -> Countdown timer
                6 -> Auto update of date and time
		7 -> Back
                """);
	inputForClockOptions();
	}

	public void inputForPhoneBook(){
			int phoneBook = scanner.nextInt();
               		switch (phoneBook) {
				case 1: System.out.println("Search");
				break;
				case 2: System.out.println("Service Nos.");
				break;
				case 3: System.out.println("Add name");
				break;
				case 4: System.out.println("Erase");
				break;
				case 5: System.out.println("Edit");
				break;
				case 6: System.out.println("Search");
				break;
				case 7: System.out.println("Service Nos.");
				break;
				case 8: phoneBookOptionEight();
				break;
				case 9: System.out.println("Speed dials");
				break;
				case 10: System.out.println("Voice Tags");
				break;
				case 11: phoneMenu();
				break;
				default : System.out.println(" Invalid Input ");
					phoneMenu();
			}
	}
	
	
	public void phoneBookOptionEight(){
		System.out.println("Options");
		System.out.println("1. Type of view\n2.Memory status\n Enter Three to go to the previous Menu or 4 to go to the main menu");
				int options = scanner.nextInt(); 
				 switch (options){
                    		case 1: System.out.println("Type of view"); 
				break;
                   	 	case 2: System.out.println("Memory status");
				break;
				case 3: displayPhoneBookOption();break;
				case 4: phoneMenu();break;
				default: System.out.println("Invalid Input");
				}
	}

	public  void inputForMessage(){
			int messages = scanner.nextInt();
               		switch (messages) {
                    		case 1: System.out.println("Write messages");
                       	 	break;
                    		case 2: System.out.println("Inbox");
                        	break;
                    		case 3: System.out.println("Outbox");
                        	break;
                    		case 4: System.out.println("Picture messages");
                        	break;
                    		case 5: System.out.println("Template");
                        	break;
                    		case 6: System.out.println("Smileys");
                        	break;
                    		case 7: messageOptionSeven();
				break;	
                    		case 8: System.out.println("Info service");
                        	break;
                    		case 9: System.out.println("Voice mailbox number");
                        	break;
                    		case 10: System.out.println("Service command editor");
                        	break;
                    		case 11: phoneMenu();
                		break;	
				default : System.out.println(" Invalid Input ");
				
				}
	}



	
	public void messageOptionSeven(){
		System.out.println("messageSettings");
		System.out.println("1. Set 1\n2.Common\n Enter Three to go to the previous Menu or 4 to go to the main menu");
				int messageSettings = scanner.nextInt(); 
				switch (messageSettings){
                    		case 1: messageOptionSevenA(); 
				break;
                   	 	case 2: messageOptionSevenB();
				break;
				case 3: messageOptionSeven();break;
				case 4: phoneMenu();break;
				default: System.out.println("Invalid Input");
				}
	}

	public void messageOptionSevenA(){
		System.out.println("set1");
		System.out.println("1. Message center number\n2.Message sent as\n3.Message validity Enter Four to go to the previous Menu or 5 to go to the main menu");
				int set1 = scanner.nextInt(); 
				switch (set1){
                    		case 1: System.out.println("Message center number"); 
				messageOptionSevenA();
				break;
                   	 	case 2: System.out.println("Message sent as");
				messageOptionSevenA();
				break;
				case 3: System.out.println("Message validity");
				messageOptionSevenA();
				break;
				case 4: messageOptionSeven();break;
				case 5: phoneMenu();break;
				default: System.out.println("Invalid Input");
				}
	}

	public void messageOptionSevenB(){
		System.out.println("common");
		System.out.println("1. Delivery report\n2.Reply via same centre\n3.Character support Enter Four to go to the previous Menu or 5 to go to the main menu");
				int common = scanner.nextInt(); 
				switch (common){
                    		case 1: System.out.println("Delivery report"); 
				messageOptionSevenB();
				break;
                   	 	case 2: System.out.println("Reply via same centre");
				messageOptionSevenB();
				break;
				case 3: System.out.println("Character support");
				messageOptionSevenB();
				break;
				case 4: messages();break;
				case 5: phoneMenu();break;
				default: System.out.println("Invalid Input");
				}
	}

	public void inputForCallRegister(){
			int callRegister = scanner.nextInt();
			switch (callRegister) {
				case 1: System.out.println("Missed calls");
				break;
				case 2: System.out.println("Recevied calls");
				break;
				case 3: System.out.println("Dialled number");
				break;
				case 4: System.out.println("Erase recent call list");
				break;
				case 5: showCallDurationOption5();
				break;
				case 6: showCallCostOption6();
				break;
				case 7: callCostSettingOption7();
				break;
				case 8: System.out.println("Prepaid credit");
				break;
				case 9: phoneMenu();break;
				default: System.out.println("Invalid Input");
				
			}

	}
	public void showCallDurationOption5(){
		System.out.println("showCallDuration");
		System.out.println("1.Last call duration\n2.All calls' duration\n3.Recieved calls' duration\n4.Dialled calls' duration\n5.Clear timers Enter Four to go to the previous Menu or 5 to go to the main menu");
			int showCallDuration = scanner.nextInt();
			switch (showCallDuration) {
				case 1: System.out.println("Last call duration");
				break;
				case 2: System.out.println("All calls' duration");
				break; 
				case 3: System.out.println("Recieved calls' duration");
				break;
				case 4: System.out.println("Dialled calls' duration");
				break;
				case 5: System.out.println("Clear timers");
				break;
				case 6: messageOptionSevenA();break;
				case 7: phoneMenu();break;
				default: System.out.println("Invalid Input");
				break;
			}

	}
		
	public void showCallCostOption6(){	
		System.out.println("showCallCost");
		System.out.println("1.Last call cost\n2.All calls cost\n3.Clear counter Enter Four to go to the previous Menu or 5 to go to the main menu");
			int showCallCost = scanner.nextInt(); 
			switch (showCallCost) {
				case 1: System.out.println("Last call cost");
				break;
				case 2: System.out.println("All calls cost");
				break; 
				case 3: System.out.println("Clear counter");
				break;
				case 4: messageOptionSevenB();break;
				case 5: phoneMenu();break;
				default: System.out.println("Invalid Input");
				break; 
			}	
	}

	public void callCostSettingOption7(){
		System.out.println("callCostSettings");		
		System.out.println("1.Last call duration\n2.All calls' duration\n3.Recieved calls' duration\n4.Dialled calls' duration\n5.Clear timers Enter Four to go to the previous Menu or 5 to go to the main menu");
			int callCostSettings = scanner.nextInt();
			switch(callCostSettings){
					case 1: System.out.println("Call cost limit");
					break;
					case 2: System.out.println("Show costs in");
					break;
					case 3: messageOptionSevenA();
					break;
					case 4: phoneMenu();
					break;
					default: System.out.println("Invalid Input");
					break;
			}

	}
	
	public void inputForTonesOptions(){
			int tones = scanner.nextInt();
			switch (tones) {
				case 1: System.out.println("Ringing tone");
				break;
				case 2: System.out.println("Ringing volume");
				break;
				case 3: System.out.println("Incoming call alert");
				break;
				case 4: System.out.println("Composer");
				break;	
				case 5: System.out.println("Message alert tone");
				break;
				case 6: System.out.println("Keypad tones");
				break;
				case 7: System.out.println("Warning and game tone");
				break;
				case 8: System.out.println("Vibrating alert");
				break;
				case 9: System.out.println("Screen saver");
				break;
				case 10: phoneMenu();break;
				default: System.out.println("Invalid Input");break;
			}	
	}

	public void inputForSettingsOptions(){
			int settings = scanner.nextInt();
			switch(settings){
				case 1: settingsOptions1();
				break;
				case 2: settingsOptions2();
				break;
				case 3: settingsOptions3();
				break;
				case 4: System.out.println("Restore factory settings");
				break;
				case 5: phoneMenu();
				break;
				default: System.out.println("Invalid Input");break;
			}

	}
	
	public void settingsOptions1(){
		System.out.println("call settings");		
		System.out.println("1.Automatic redial\n2.Speed dialling\n3.Call waiting options\n4.Own number sending\n5.Phone line in use\n6.Automatic answer Enter Four to go to the previous Menu or 5 to go to the main menu");
			int callSettings = scanner.nextInt();
			switch(callSettings){
				case 1: System.out.println("Automatic redial");
				break;
				case 2: System.out.println("Speed dialling");
				break;
				case 3: System.out.println("Call waiting options");
				break;
				case 4: System.out.println("Own number sending");
				break;
				case 5: System.out.println("Phone line in use");
				break;
				case 6: System.out.println("Automatic answer");
				break;
				case 7: phoneMenu();
				break;
				default: System.out.println("Invalid Input");break;
			}

	}


	public void settingsOptions2(){
		System.out.println("phoneSettings");		
		System.out.println("1.Last call duration\n2.All calls' duration\n3.Recieved calls' duration\n4.Dialled calls' duration\n5.Clear timers Enter Four to go to the previous Menu or 5 to go to the main menu");
			int phoneSettings = scanner.nextInt();
			switch(phoneSettings){
				case 1: System.out.println("Language");
				break;
				case 2: System.out.println("Cell info display");
				break;
				case 3: System.out.println("Welcome note");
				break;
				case 4: System.out.println("Network selection");
				break;
				case 5: System.out.println("Lights");
				break;
				case 6: System.out.println("Confirm SIM service");
				break;
				case 7: phoneMenu();
				break;
				default: System.out.println("Invalid Input");
				break;
			}
	}

	
	public void settingsOptions3(){
		System.out.println("securitySettings");		
		System.out.println("1.PIN code request\n2.Call info display\n3.Fixed dialling\n4.Closed user group\n5.Phone security\n6.Change access codes Enter Four to go to the previous Menu or 5 to go to the main menu");
			int securitySettings = scanner.nextInt();
			switch(securitySettings){
				case 1: System.out.println("PIN code request");
				break;
				case 2: System.out.println("Call info display");
				break;
				case 3: System.out.println("Fixed dialling");
				break;
				case 4: System.out.println("Closed user group");
				break;
				case 5: System.out.println("Phone security");
				break;
				case 6: System.out.println("Change access codes");
				break;
				case 7: phoneMenu();
				break;
				default: System.out.println("Invalid Input");
				break; 
			}

	}

	public void inputForClockOptions(){
			int clock = scanner.nextInt();
			switch (clock) {
				case 1: System.out.println("Alarm clock");
				break;
				case 2: System.out.println("Clock settings");
				break;
				case 3: System.out.println("Date setting");
				break;
				case 4: System.out.println("Stopwatch");
				break;
				case 5: System.out.println("Countdown timer");
				break;
				case 6: System.out.println("Auto update of date and time");
				break;
				case 7: phoneMenu();
				break;
				default: System.out.println("Invalid Input");
				break; 
			}
	}
	
	
	



		

				
}