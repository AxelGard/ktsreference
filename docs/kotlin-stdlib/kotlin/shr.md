

# shr

Shifts this value right by the n number of bits, filling the leftmost bits with copies of the sign bit.

```kotlin
infix inline fun BigInteger.shr(n: Int): BigInteger(source)
```

```kotlin
import java.math.BigInteger

fun main() {
    val original = BigInteger("1024")   // 0b10000000000
    val shifted = original shr 4        // shift right by 4 bits → 0b100000000
    println("Original: $original")      // 1024
    println("Shifted right by 4 bits: $shifted") // 64
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/shr.html)

    