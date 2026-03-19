

# or

Performs a bitwise OR operation between the two values.

```kotlin
infix inline fun BigInteger.or(other: BigInteger): BigInteger(source)
```

```kotlin
import java.math.BigInteger

fun main() {
    val a = BigInteger("1010", 2) // binary 1010
    val b = BigInteger("1100", 2) // binary 1100

    val result = a or b

    println("a: ${a.toString(2)}")
    println("b: ${b.toString(2)}")
    println("a OR b: ${result.toString(2)}") // prints 1110
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/or.html)

    