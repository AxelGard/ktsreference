

# getOwner

Returns the owner of a file.

```kotlin
inline fun Path.getOwner(vararg options: LinkOption): UserPrincipal?(source)
```

```kotlin
import java.nio.file.LinkOption
import kotlin.io.path.Path
import kotlin.io.path.exists
import kotlin.io.path.getOwner

fun main() {
    val file = Path("sample.txt")
    if (!file.exists()) {
        println("File not found.")
        return
    }

    // Retrieve the owner, following symbolic links by default.
    val owner = file.getOwner()               // or file.getOwner(LinkOption.NOFOLLOW_LINKS)
    println("Owner of ${file.fileName}: ${owner?.name}")
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/get-owner.html)

    