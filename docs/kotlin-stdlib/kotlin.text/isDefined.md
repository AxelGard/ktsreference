

# isDefined

Returns true if this character (Unicode code point) is defined in Unicode.

```kotlin
expect fun Char.isDefined(): Boolean(source)
```

```kotlin
fun main() {
    val definedChar = 'ℑ'          // Greek letter Iota
    val undefinedChar = '\uFFFF'   // Undefined Unicode code point

    println("Is '${definedChar}' defined? ${definedChar.isDefined()}")   // true
    println("Is '\\uFFFF' defined? ${undefinedChar.isDefined()}")        // false
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/is-defined.html)

    