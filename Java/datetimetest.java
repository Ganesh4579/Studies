import java.time.Clock;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.MonthDay;
import java.time.OffsetTime;
import java.time.Period;
import java.time.Year;
import java.time.ZoneId;
import java.time.ZoneOffset;
import java.time.ZonedDateTime;
import java.time.temporal.ChronoField;

public class datetimetest {
    public static void main(String a[]) {
        java.time.LocalDate ld = LocalDate.now();
        java.time.LocalDate ld1 = LocalDate.of(1999, 11, 26);
        java.time.LocalTime lt = LocalTime.now();
        System.out.println(ld + "  " + ld1);
        System.out.println(ld.atTime(lt));
        System.out.println(ld.isLeapYear());
        System.out.println("\n\n");

        ///

        java.time.MonthDay md = MonthDay.now();
        System.out.println(md);
        System.out.println(md.atYear(2020));
        System.out.println("\n\n");

        ///

        java.time.OffsetTime ot = OffsetTime.now();
        System.out.println(ot);
        System.out.println("\n\n");

        ///

         System.out.println(Clock.systemUTC().getZone());
         System.out.println(Clock.systemUTC().instant());
         System.out.println("\n\n");

        ///

        ZonedDateTime zone = ZonedDateTime.parse("2016-10-05T08:20:10+05:30[Asia/Kolkata]");  
        System.out.println(zone);  
        System.out.println("\n\n");

        ///

        System.out.println(ZoneOffset.UTC);
        System.out.println(ZoneOffset.MIN);
        System.out.println(ZoneOffset.ofHours(4));
        System.out.println("\n\n");

        ///


        Year y = Year.now();  
        Year y1 = Year.of(1100); 
        System.out.println(y);
        System.out.println(y.atDay(200));
        System.out.println(y.isLeap());
        System.out.println(y.isBefore(y1));
        System.out.println("\n\n");

        ///

        System.out.println(ChronoField.MONTH_OF_YEAR);
        System.out.println("\n\n");

        ///

        System.out.println( Period.ofDays(2).addTo(LocalDate.now()));


    }
}