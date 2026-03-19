

# toCharArray

Returns an array of Char containing all of the elements of this generic array.

```kotlin
fun Array<out Char>.toCharArray(): CharArray(source)
```

```kotlin
fun main() {
    val chars: Array<Char> = arrayOf('K', 'o', 't', 'l', 'i', 'n')
    val charArray: CharArray = chars.toCharArray()
    println(charArray.joinToString(" ")) // Output: K o t l i n
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-char-array.html)

    