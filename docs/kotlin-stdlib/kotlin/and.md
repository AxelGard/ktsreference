

# and

Performs a bitwise AND operation between the two values.

```kotlin
infix inline fun BigInteger.and(other: BigInteger): BigInteger(source)
```

```kotlin
import java.math.BigInteger

fun main() {
    val a = BigInteger("15")   // binary 1111
    val b = BigInteger("9")    // binary 1001
    val c = a and b            // binary AND: 1001 (9)
    println(c)                 // prints 9
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/and.html)

    