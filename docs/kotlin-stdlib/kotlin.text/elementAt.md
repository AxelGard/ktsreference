

# elementAt

Returns a character at the given index or throws an IndexOutOfBoundsException if the index is out of bounds of this char sequence.

```kotlin
expect fun CharSequence.elementAt(index: Int): Char(source)
```

```kotlin
val text = "Hello, Kotlin!"
val index = 7

val character = text.elementAt(index)
println("Character at index $index is '$character'")  // prints: Character at index 7 is 'K'
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/element-at.html)

    