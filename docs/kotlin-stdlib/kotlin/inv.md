

# inv

Inverts the bits including the sign bit in this value.

```kotlin
inline fun BigInteger.inv(): BigInteger(source)
```

```kotlin
import java.math.BigInteger

fun main() {
    val original = BigInteger("15")          // binary: 1111
    val inverted = original.inv()            // bitwise NOT -> -16
    println("Original: $original")           // 15
    println("Inverted: $inverted")           // -16
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/inv.html)

    