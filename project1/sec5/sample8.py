#입금, 출금, 잔액 조회가 가능한 은행 계좌관리 프로그램을 작성하여라
#잔액(balance), 입출금액(money), 계좌번호(idNum), 계좌주(idName)
#입금기능(deposit), 출금기능(withdraw), 잔액조회(getBalance)
#클래스의 멤버를 선언하여 작동될 수 있도록 할 것

class BankApplication {
private static Account2[] accountArray = new Account2[100]
private static Scanner scanner = new Scanner(System.in )

public static void main(String[] args) {
boolean run = true


while (run){
System.out.println("-----------------------------------------------")
System.out.println("1.계좌생성 | 2.계좌목록 | 3.예금 | 4.출금 | 5.종료")
System.out.println("-----------------------------------------------")
System.out.print("선택 > ")

int selectNo = scanner.nextInt()

if (selectNo == 1){
createAccount();
} else if (selectNo == 2){
accountList();
} else if (selectNo == 3){
deposit();
} else if (selectNo == 4){
withdraw();
} else if (selectNo == 5){
run = false
}
}
System.out.println("프로그램 종료")
}


private
static
void
createAccount()
{
System.out.println("--------------")
System.out.println("  계좌 생성   ")
System.out.println("--------------")

System.out.print("계좌번호 : ")
String
ano = scanner.next();

System.out.print("계좌주 : ")
String
owner = scanner.next()

System.out.print("초기 입금액 : ")
int
balance = scanner.nextInt()

Account2
acc = new
Account2(ano, owner, balance)

for (int i=0;i < accountArray.length;i++){
if (accountArray[i] == null){
accountArray[i] = acc
System.out.println("결과 : 계좌가 생성되었습니다.")
break
}
}
}


private
static
void
accountList()
{
    System.out.println("--------------")
System.out.println("  계좌 목록   ")
System.out.println("--------------")
System.out.println("계좌번호\t계좌주\t잔액")
for (int i=0;i < accountArray.length;i++)
{
if (accountArray[i] == null)
break
System.out.println(accountArray[i].getAno() + "\t"
                   + accountArray[i].getOwner() + "\t"
                   + accountArray[i].getBalance())
}
}


private
static
void
deposit()
{
    System.out.println("--------------")
System.out.println("  예금하기   ")
System.out.println("--------------")

System.out.print("계좌번호 : ")
String
ano = scanner.next()

System.out.print("예금액 : ")
int
balance = scanner.nextInt()

Account2
acc = findAccount(ano)

if (acc == null)
{
System.out.println("결과 : 계좌가 존재하지 않습니다.")
return
}

acc.setBalance(acc.getBalance() + balance);
System.out.println("결과 : " + balance + "가 성공적으로 입금처리 되었습니다.")
}


private
static
void
withdraw()
{
    System.out.println("--------------")
System.out.println("  출금하기   ")
System.out.println("--------------")

System.out.print("계좌번호 : ")
String
ano = scanner.next()

System.out.print("출금액 : ")
int
balance = scanner.nextInt()

Account2
acc = findAccount(ano)

if (acc == null)
{
System.out.println("결과 : 계좌가 존재하지 않습니다.");
return
}

if (acc.getBalance() < balance) {
System.out.println("예금액이 출금액보다 적어서 출금할 수 없습니다.")
return
}

acc.setBalance(acc.getBalance() - balance);
System.out.println("결과 : " + balance + "가 성공적으로 출금처리 되었습니다.")
}


private
static
Account2
findAccount(String
ano){
    Account2
acc = null
for (int i=0;i < accountArray.length;i++)
{
if (accountArray[i] != null){
if (accountArray[i].getAno().equals(ano)){
acc = accountArray[i]
break
}
}
}
return acc
}
}