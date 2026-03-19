

# and

 [kotlin-stdlib](/kotlin-stdlib) / [kotlin](/kotlin-stdlib/kotlin) / [and](kotlin-stdlib/kotlin/and)

Performs a bitwise AND operation between the two values.

```kotlin
infix inline fun BigInteger.and(other: BigInteger): BigInteger(source)
```

```kotlin
import java.math.BigInteger

fun main() {
    val a = BigInteger("0b1101", 2)   // 13
    val b = BigInteger("0b1011", 2)   // 11

    val result = a and b              // bitwise AND

    println(result)                   // prints 9
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/and.html)

    