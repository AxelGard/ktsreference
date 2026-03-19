

# and

Performs a bitwise AND operation between the two values.

```kotlin
infix inline fun BigInteger.and(other: BigInteger): BigInteger(source)
```

```kotlin
import java.math.BigInteger

fun main() {
    val a = BigInteger("15")   // binary 1111
    val b = BigInteger("10")   // binary 1010

    val c = a and b            // infix usage of BigInteger.and

    println("$a AND $b = $c")  // prints: 15 AND 10 = 10
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/and.html)

    