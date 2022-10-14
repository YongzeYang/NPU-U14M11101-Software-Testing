package net.mooctest;

import org.junit.After;
import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.ExpectedException;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;

import static net.mooctest.Nextday.nextDay;
import static org.junit.Assert.*;

public class NextDayTest {

    @Rule
    public ExpectedException thrown = ExpectedException.none();

    private final ByteArrayOutputStream outputStreamCaptor = new ByteArrayOutputStream();

    @Before
    public void setUp() throws Exception {
        System.setOut(new PrintStream(outputStreamCaptor));
    }

    @After
    public void tearDown() throws Exception {
        try {
            outputStreamCaptor.flush();
            outputStreamCaptor.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    @Test
    public void testDate() {
        Date date1 = new Date(2,29,4);
        Date date2 = new Date(12,31,4);
        date1.increment();
        date2.increment();
        date1.printDate();
        assertEquals(date1.toString(),outputStreamCaptor.toString().trim());
        assertEquals(date2,nextDay(new Date(12,31,4)));
        assertFalse(date1.equals(date2));
    }

    @Test
    public void testMonth() {
        Month inleap = new Month(12,new Year(1));
        Month leap = new Month(2,new Year(4));
        assertEquals(29,leap.getMonthSize());
        assertEquals(31,inleap.getMonthSize());

        assertTrue(leap.increment());
        assertFalse(inleap.increment());
        assertFalse(inleap.equals(leap));

        thrown.expect(IllegalArgumentException.class);
        thrown.expectMessage("Not a valid month");
        new Date(13, 1,1);

    }

    @Test
    public void testDay() {
        Day day1 = new Day(28,new Month(2,new Year(1)));
        Day day2 = new Day(27,new Month(2,new Year(1)));
        assertTrue(day2.increment());
        assertFalse(day1.increment());
        assertFalse(day1.equals(day2));

        thrown.expect(IllegalArgumentException.class);
        thrown.expectMessage("Not a valid day");
        new Date(2, 30,1);
    }

    @Test
    public void testYear() {
        Year year1 = new Year(-1);
        assertTrue(year1.increment());
        assertTrue(new Year(-5).isLeap());
        assertTrue(new Year(4).isLeap());
        assertFalse(year1.equals(new Year(-1)));

        thrown.expect(IllegalArgumentException.class);
        thrown.expectMessage("Not a valid month");
        new Date(1, 1,0);
    }

}