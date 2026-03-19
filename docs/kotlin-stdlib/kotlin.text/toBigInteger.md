

# toBigInteger

Parses the string as a java.math.BigInteger number and returns the result.

```kotlin
inline fun String.toBigInteger(): BigInteger(source)
```

```kotlin
import java.math.BigInteger

fun main() {
    val bigInt = "12345678901234567890".toBigInteger()
    println("BigInteger: $bigInt")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-big-integer.html)

    