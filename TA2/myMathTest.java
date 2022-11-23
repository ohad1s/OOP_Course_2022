package TA2;

import static org.junit.jupiter.api.Assertions.*;

class myMathTest {

    @org.junit.jupiter.api.Test
    void compare() {
        assertTrue(myMath.compare(myMath.mul(3, 5), myMath.plus(10, 5)));
        assertFalse(myMath.compare(10, 12));
    }

    @org.junit.jupiter.api.Test
    void plus() {
        assertAll(() -> assertEquals(4, myMath.plus(2, 2)),
                () -> assertEquals(-4, myMath.plus(2, -2)),
                () -> assertEquals(4, myMath.plus(-2, -2)),
                () -> assertEquals(0, myMath.plus(1, 0)));
        assertEquals(5, myMath.plus(2, 3));
    }

    @org.junit.jupiter.api.Test
    void minus() {
        assertEquals(myMath.minus(3, 2), 1);
    }

    @org.junit.jupiter.api.Test
    void divide() {
        Exception e = assertThrows(ArithmeticException.class, () -> myMath.divide(5, 0));
        assertEquals("/ by zero", e.getMessage());
    }
}