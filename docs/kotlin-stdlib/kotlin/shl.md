

# shl

Shifts this value left by the n number of bits.

```kotlin
infix inline fun BigInteger.shl(n: Int): BigInteger(source)
```

```kotlin
import java.math.BigInteger

fun main() {
    val original = BigInteger("5")
    val shifted = original shl 3   // shift left by 3 bits
    println(shifted)                // prints 40
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/shl.html)

    