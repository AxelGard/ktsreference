

# mod

Calculates the remainder of flooring division of this value (dividend) by the other value (divisor).

```kotlin
inline fun Byte.mod(other: Byte): Byte(source)
```

```kotlin
fun main() {
    val dividend: Byte = 10
    val divisor: Byte = 3

    val remainder: Byte = dividend.mod(divisor)

    println("The remainder of $dividend ÷ $divisor is $remainder") // Output: 1
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/mod.html)

    