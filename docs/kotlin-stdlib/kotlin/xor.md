

# xor

Performs a bitwise XOR operation between the two values.

```kotlin
infix inline fun BigInteger.xor(other: BigInteger): BigInteger(source)
```

```kotlin
import java.math.BigInteger

fun main() {
    val a = BigInteger("1010", 2)  // binary 1010 (decimal 10)
    val b = BigInteger("1100", 2)  // binary 1100 (decimal 12)

    val result = a xor b          // bitwise XOR

    println("Result in binary: ${result.toString(2)}")  // prints 110
    println("Result in decimal: $result")                // prints 6
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/xor.html)

    