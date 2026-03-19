

# isLowSurrogate

Returns true if this character is a Unicode low-surrogate code unit (also known as trailing-surrogate code unit).

```kotlin
expect fun Char.isLowSurrogate(): Boolean(source)
```

```kotlin
fun main() {
    val highSurrogate = '\uD834'
    val lowSurrogate = '\uDD1E'

    println(highSurrogate.isLowSurrogate()) // false
    println(lowSurrogate.isLowSurrogate())  // true
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/is-low-surrogate.html)

    